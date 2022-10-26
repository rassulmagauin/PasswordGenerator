from django.shortcuts import render
from django.http import HttpResponse
import random
from generator.models import Passwords
from .models import Passwords

# Create your views here.

def home(request):
    passwords = Passwords.objects.all().order_by('-created')[:5]
    for password in passwords:
        print(password.title+" "+(str)(password.created))
    return render(request, 'generator/home.html', {'passwords':passwords})

def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFJHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()[]\'/.'))
    thepassword = ''
    for x in range(length):
        thepassword+=random.choice(characters)
    p = Passwords(title = thepassword)
    p.save()
    return render(request, 'generator/password.html', {'password':thepassword})

def aboutus(request):
    return render(request, 'generator/aboutus.html')
