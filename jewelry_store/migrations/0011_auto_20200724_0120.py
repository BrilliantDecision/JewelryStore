# Generated by Django 3.0.8 on 2020-07-23 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_store', '0010_auto_20200723_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус заказа'),
        ),
    ]