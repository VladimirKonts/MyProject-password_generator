from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):



    characters = list('qwertyuioplkjhgfdsazxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()<>?{}'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 19))

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


    # Create your views here.
def more(request):

    greeting = 'This is just the beginning'

    return render(request, 'generator/more.html', {'more': greeting})