from celery import shared_task
from django.conf import settings
from django_ethereum_events.web3_service import Web3Service
import requests
from datetime import date, timedelta
from .models import Transactions

CURRENCY_CODE = ''
CURRENCY_RATE = 0




@shared_task
def poll_price():

    web3 = Web3Service().web3
    ABI = settings.ORACLE_CONTRACT_ABI
    ADDRESS = settings.ORACLE_CONTRACT_ADDRESS
   
    token_contract = web3.eth.contract(address=ADDRESS, abi=ABI)
    PRIVATE_KEY = settings.PRIVATE_KEY

    #  API CALL
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=xdce-crowd-sale&vs_currencies=usd')
    print("response", response.json())
    data = response.json()
    CURRENCY_RATE = data['xdce-crowd-sale']['usd']
    CURRENCY_RATE = int(CURRENCY_RATE * 10**18)
    account_1 = "0xd1b8C6d6698b4484dAA008e1a03f51e1F1c8b1d5"
    nonce = web3.eth.getTransactionCount(account_1)
    # send transaction set method on contract
    tx_hash = token_contract.functions.set(CURRENCY_RATE).buildTransaction({
        'chainId':51,
        'gas': 65000,
        'gasPrice': web3.toWei(10, 'gwei'),
        'from': account_1,
        'nonce': nonce
    })
    signed_tx = web3.eth.account.signTransaction(tx_hash, private_key=PRIVATE_KEY)
    new_tx_hash = web3.toHex(web3.keccak(signed_tx.rawTransaction))
    res = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    txhash = web3.toHex(res)
    # get transaction receipt
    receipt = web3.eth.waitForTransactionReceipt(txhash)
    print("tx_receipt", receipt)

    Transactions.objects.create(amount=CURRENCY_RATE, gas_used=receipt.cumulativeGasUsed)