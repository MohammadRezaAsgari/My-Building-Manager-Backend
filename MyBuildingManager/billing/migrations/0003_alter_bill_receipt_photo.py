# Generated by Django 4.2.7 on 2023-12-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_bill_payment_status_bill_receipt_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='receipt_photo',
            field=models.FileField(blank=True, null=True, upload_to='uploads/receipt_photo/'),
        ),
    ]
