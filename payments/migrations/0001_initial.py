# Generated by Django 3.2.7 on 2021-09-13 09:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
            options={
                'db_table': 'tbl_payment_methods',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_receipt_no', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_reference_id', models.UUIDField(blank=True, null=True)),
                ('transaction_status', models.CharField(blank=True, max_length=100, null=True)),
                ('completed_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.paymentmethods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
            options={
                'db_table': 'tbl_payments',
                'ordering': ['created_at', 'amount'],
            },
        ),
        migrations.CreateModel(
            name='MpesaPayments',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('phone_no', models.CharField(max_length=50)),
                ('merchant_request_id', models.CharField(blank=True, max_length=200, null=True)),
                ('conversation_id', models.CharField(blank=True, max_length=200, null=True)),
                ('originator_conversation_id', models.CharField(blank=True, max_length=200, null=True)),
                ('checkout_request_id', models.CharField(blank=True, max_length=200, null=True)),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('mpesa_code', models.CharField(blank=True, max_length=50, null=True)),
                ('response_code', models.CharField(blank=True, max_length=50, null=True)),
                ('order_id', models.UUIDField(blank=True, null=True)),
                ('transaction_status', models.CharField(blank=True, max_length=100, null=True)),
                ('completed_time', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('response_description', models.CharField(blank=True, max_length=100, null=True)),
                ('transaction_type', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
            options={
                'db_table': 'tbl_mpesa_payments',
                'ordering': ['created_at', 'amount'],
            },
        ),
    ]
