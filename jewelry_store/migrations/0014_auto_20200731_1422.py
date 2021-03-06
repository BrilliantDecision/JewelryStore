# Generated by Django 3.0.8 on 2020-07-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_store', '0013_auto_20200730_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount_gems',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество камней (данного типа)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество товара на складе'),
        ),
    ]
