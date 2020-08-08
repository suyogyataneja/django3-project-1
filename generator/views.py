from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

#def home(request):
#    return HttpResponse('I am the best ')

#USING Render function here that allows you to pass a template
def home(request):
    return render(request,'generator/home.html',{'password':'dsjhs'})
def eggs(request):
    return HttpResponse('<h1>EGGS ARE AMAZING</h1>')

def password(request):

    the_password='testing'

    characters = list('abacdefeghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length',12))

    the_password = ''
    for i in range(length):
        the_password+=random.choice(characters)
    return render(request,'generator/password.html',{'password':the_password})