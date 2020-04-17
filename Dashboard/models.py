from django.db import models
from _datetime import  date
from django.utils import timezone
from django.contrib.auth.models import User

DEPARTMENT = (
    ("CSE",'COMPUTER SCIENCE ENGINEERING'),
    ("ECE",'ELECTRONCS AND COMMUNICATION ENGINEERING'),
    ('IT','INFORMATION TECHNOLOGY'),
    ('CE','CIVIL ENGINEERING'),
    ('AE','AERONAUTICAL ENGINEERING'),
    ('EEE','ELECTRICAL AND ELECTRONICS ENGINEERING'),
    ('EI','ELECTRICAL INSTRUMENTATION'),
    ('FT','FASHION TECHNOLOGY'),
    ('ISE','INFORMATION SCIENCE ENGINEERING'),
    ('TXT','TEXITLE ENGINEERING')
)
class DS(models.Model):
    full_name = models.CharField(verbose_name='full name of student',max_length=500)
    initial = models.CharField(max_length=10,verbose_name='initial of student')
    roll_no = models.CharField(max_length=8,primary_key=True,help_text='do not fill this! office use only',blank=True)
    dept = models.CharField(default=0,choices=DEPARTMENT,verbose_name='department going to choose',max_length=500)
    email_id = models.EmailField(default='@gmail.com',unique=True,verbose_name='email of student personal',help_text='personal mail id')
    email_id_college = models.EmailField(unique=True,verbose_name='email to be given in school',help_text='for office purpose only')
    phone_number = models.IntegerField(default=0,unique=True,verbose_name='phone number used for further college purpose',help_text="use students else parents number")
    address = models.CharField(default="#address",max_length=5000,verbose_name='permanent address',help_text='permanent address')
    school_details = models.CharField(default=0,max_length=5000,verbose_name='HSC school details',help_text='HSC school details')
    is_staff = models.BooleanField(default=False)
