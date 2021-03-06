# Generated by Django 3.0.8 on 2020-07-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_store', '0005_auto_20200722_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveSmallIntegerField(default=0, help_text='шт', verbose_name='Количество камней (данного типа)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_material',
            field=models.FloatField(default=0, help_text='граммы', verbose_name='Вес металла'),
        ),
    ]
