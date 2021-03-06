# Generated by Django 3.2.7 on 2021-09-13 11:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('direction', models.CharField(choices=[('dr', 'Dr'), ('cr', 'Cr')], max_length=10)),
                ('type', models.CharField(choices=[('withdrawal', 'WITHDRAW'), ('wallet_deposit', 'WALLET_DEPOSIT'), ('wallet_withdraw', 'WALLET_WITHDRAW'), ('reversal', 'REVERSAL')], max_length=30)),
                ('currency_code', models.CharField(max_length=10)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('wallet_balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallets.wallet')),
            ],
            options={
                'db_table': 'tbl_transactions',
                'ordering': ['created_at', 'amount'],
            },
        ),
    ]
