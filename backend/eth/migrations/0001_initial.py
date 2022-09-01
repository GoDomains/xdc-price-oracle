# Generated by Django 3.2.6 on 2022-08-01 06:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockChainTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_hash', models.CharField(blank=True, default='', max_length=66)),
                ('status', models.BooleanField(default=False)),
                ('method', models.CharField(blank=True, default='', max_length=200)),
                ('params', models.TextField(blank=True, default='')),
                ('message', models.TextField(blank=True, default='')),
                ('executor', models.CharField(blank=True, default='', max_length=42)),
                ('contract', models.CharField(blank=True, default='', max_length=42)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'BlockChain Transactions',
            },
        ),
        migrations.CreateModel(
            name='EventsLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_hash', models.CharField(blank=True, default='', max_length=66)),
                ('event_name', models.CharField(blank=True, default='', max_length=200)),
                ('event_data', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Events Log',
            },
        ),
        migrations.CreateModel(
            name='TransactionAction',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('transaction_hash', models.CharField(blank=True, default='', max_length=66)),
                ('status', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'Transaction Actions',
            },
        ),
    ]
