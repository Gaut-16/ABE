# Generated by Django 2.2.12 on 2020-04-15 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0008_auto_20200415_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ds',
            name='Student_image',
        ),
    ]
