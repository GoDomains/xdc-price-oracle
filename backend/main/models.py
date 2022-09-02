from django.db import models

# Create your models here.
class Transactions(models.Model):
    amount = models.BigIntegerField()
    gas_used = models.BigIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount) + " " + str(self.gas_used) + " " + str(self.timestamp)