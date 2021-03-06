# Generated by Django 3.0.8 on 2020-07-23 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_store', '0007_auto_20200723_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allpurchases',
            name='price',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.AlterField(
            model_name='allpurchases',
            name='amount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewelry_store.Client', verbose_name='Номер клиента'),
        ),
    ]
