# Create your views here.
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
class UserForm(forms.Form):
    username = forms.CharField()


def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            request.session['username'] = username
            return HttpResponseRedirect('/index/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})          


def index(request):
    username = request.session.get('username','anybody')
    return render_to_response('index.html',{'username':username})


def logout(request):
    del request.session['username']
    return HttpResponse('logout ok')
