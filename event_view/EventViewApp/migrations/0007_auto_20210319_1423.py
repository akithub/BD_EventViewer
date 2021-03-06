# Generated by Django 3.1.2 on 2021-03-19 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EventViewApp', '0006_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='period',
            field=models.IntegerField(choices=[(1, 'Daily'), (2, 'Temporarily'), (3, 'Forever'), (4, 'Guild'), (5, 'Buff'), (6, 'Login'), (7, 'Season'), (8, 'Perl')]),
        ),
    ]
