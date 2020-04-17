import re
from django import forms
from .models import *
from django.contrib.auth.models import User
class new_reg_student_form(forms.ModelForm):
    # def __init__(self):
    #     super(new_reg_student_form, self).__init__()


    class Meta:
        model=DS
        fields = ['full_name','initial','roll_no','dept','email_id','email_id_college','phone_number','address','school_details']


    def save(self,commit=True):
        data = self.cleaned_data
        full_name =data['full_name']
        initial =data['initial']
        roll_no = data['roll_no']
        dept =data['dept']
        email_id =data['email_id']
        email_id_college = data['email_id_college']
        if len(re.findall(r'^([a-z]*)(\.)([a-z]{1})(\.)([a-z]{3})(@kct.ac.in)$',email_id_college))==1:
            is_staff = True
        else:
            is_staff =False
        phone_number =data['phone_number']
        address = data['address']
        school_details =data['school_details']
        DS.objects.create(full_name=full_name,initial=initial,is_staff=is_staff,address=address,roll_no=roll_no,dept=dept,email_id=email_id,email_id_college=email_id_college,phone_number=phone_number,school_details=school_details)


class authuser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','repassword']

    