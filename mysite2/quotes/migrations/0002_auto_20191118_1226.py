# Generated by Django 2.2.7 on 2019-11-18 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quotaprice',
            new_name='quoteprice',
        ),
    ]