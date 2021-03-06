# Generated by Django 3.0.8 on 2020-07-23 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_store', '0006_auto_20200722_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='allpurchases',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='руб.', verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='allpurchases',
            name='amount',
            field=models.PositiveSmallIntegerField(default=0, help_text='шт.', verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jewelry_store.Client', verbose_name='Номер клиента'),
        ),
    ]
