# Generated by Django 5.1.1 on 2024-10-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_customer_email_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
