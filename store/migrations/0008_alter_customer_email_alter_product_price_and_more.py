# Generated by Django 5.1.1 on 2024-10-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_customer_email_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, max_length=13),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.FloatField(default=0, max_length=13),
        ),
    ]
