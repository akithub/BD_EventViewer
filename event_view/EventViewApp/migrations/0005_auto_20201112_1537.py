# Generated by Django 3.1.1 on 2020-11-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventViewApp', '0004_auto_20201028_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='period',
            field=models.IntegerField(choices=[(1, 'Daily'), (2, 'Temporarily'), (3, 'Forever'), (4, 'Guild'), (5, 'Buff')]),
        ),
    ]