# Generated by Django 5.1.4 on 2025-02-26 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='creaed',
            new_name='created',
        ),
    ]
