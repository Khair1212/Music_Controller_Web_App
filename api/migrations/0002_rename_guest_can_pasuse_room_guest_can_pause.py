# Generated by Django 4.0.4 on 2022-07-19 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='guest_can_pasuse',
            new_name='guest_can_pause',
        ),
    ]
