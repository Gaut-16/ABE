# Generated by Django 2.2.12 on 2020-04-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_auto_20200415_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='ds',
            name='Student_image',
            field=models.ImageField(blank=True, height_field=500, upload_to='', verbose_name='image of student', width_field=500),
        ),
        migrations.AddField(
            model_name='ds',
            name='address',
            field=models.CharField(default='#address', help_text='permanent address', max_length=5000, verbose_name='permanent address'),
        ),
        migrations.AddField(
            model_name='ds',
            name='email_id_college',
            field=models.EmailField(blank=True, help_text='for office purpose only', max_length=254, unique=True, verbose_name='email to be given in school'),
        ),
        migrations.AddField(
            model_name='ds',
            name='phone_number',
            field=models.IntegerField(default=0, help_text='use students else parents number', unique=True, verbose_name='phone number used for further college purpose'),
        ),
        migrations.AddField(
            model_name='ds',
            name='school_details',
            field=models.CharField(default=0, help_text='HSC school details', max_length=5000, verbose_name='HSC school details'),
        ),
    ]
