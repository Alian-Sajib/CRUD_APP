# Generated by Django 5.0.1 on 2024-06-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_stock_close_alter_stock_date_alter_stock_high_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.CharField(max_length=50),
        ),
    ]
