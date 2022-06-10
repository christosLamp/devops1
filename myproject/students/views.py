from dataclasses import fields
import imp
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from students.forms import StudentSignUpForm
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from django.core.mail import EmailMessage 
from .token import account_activation_token  
from django.contrib.auth import get_user_model
from students.models import Student
# from courses.models import Course
from applies.models import Apply
from secretary.models import Secretary

def apply(request):
    current_user = request.user
    apply = Apply.objects.get(student=Student.objects.get(user=current_user))
    if apply.status == '1':
        data = "Approved"
    elif apply.status == '2':
        data = "Disapproved"
    else:
        data = "Pending"
    student = Student.objects.get(user=current_user)
    context = {'data' : data}
    return render(request,'students/apply.html',{'data': data,'student': student,'user':current_user})
