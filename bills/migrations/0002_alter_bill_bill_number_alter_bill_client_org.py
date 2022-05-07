# Generated by Django 4.0.4 on 2022-05-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_number',
            field=models.IntegerField(default=1, unique=True, verbose_name='номер счета'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='client_org',
            field=models.CharField(default='', max_length=30, unique=True, verbose_name='организация клиента'),
        ),
    ]
