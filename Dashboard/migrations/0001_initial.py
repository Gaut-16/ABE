# Generated by Django 2.2.12 on 2020-04-15 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DS',
            fields=[
                ('full_name', models.CharField(max_length=500, verbose_name='full name of student')),
                ('initial', models.CharField(max_length=10, verbose_name='initial of student')),
                ('roll_no', models.CharField(blank=True, help_text='do not fill this! office use only', max_length=8, primary_key=True, serialize=False)),
                ('dept', models.CharField(choices=[('CSE', 'COMPUTER SCIENCE ENGINEERING'), ('ECE', 'ELECTRONCS AND COMMUNICATION ENGINEERING'), ('IT', 'INFORMATION TECHNOLOGY'), ('CE', 'CIVIL ENGINEERING'), ('AE', 'AERONAUTICAL ENGINEERING'), ('EEE', 'ELECTRICAL AND ELECTRONICS ENGINEERING'), ('EI', 'ELECTRICAL INSTRUMENTATION'), ('FT', 'FASHION TECHNOLOGY'), ('ISE', 'INFORMATION SCIENCE ENGINEERING'), ('TXT', 'TEXITLE ENGINEERING')], max_length=500, verbose_name='department going to choose')),
                ('year_of_join', models.DateField(default=datetime.datetime(2020, 4, 15, 10, 4, 4, 174385, tzinfo=utc), verbose_name='joining year in college')),
                ('email_id', models.EmailField(help_text='personal mail id', max_length=254, unique=True, verbose_name='email of student personal')),
                ('email_id_college', models.EmailField(blank=True, help_text='for office purpose only', max_length=254, unique=True, verbose_name='email to be given in school')),
                ('phone_number', models.IntegerField(help_text='use students else parents number', unique=True, verbose_name='phone number used for further college purpose')),
                ('address', models.CharField(help_text='permanent address', max_length=5000, verbose_name='permanent address')),
                ('Student_image', models.ImageField(height_field=500, upload_to='', verbose_name='image of student', width_field=500)),
                ('school_details', models.CharField(help_text='HSC school details', max_length=5000, verbose_name='HSC school details')),
            ],
        ),
    ]
