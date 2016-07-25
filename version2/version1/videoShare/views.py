# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
from videoShare.models import User, Video
from django.http import HttpResponseRedirect


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    headImage = forms.FileField(required=False)


def register(request):
    if  request.method == 'POST':
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            #print uf.cleaned_data['username']
            #print request.FILES
            #fp = file('upload/' + uf.cleaned_data['headImage'].name, 'wb')
            #s = uf.cleaned_data['headImage'].read()
            #fp.write(s)
            #fp.close()
            newusername = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            headImage = uf.cleaned_data['headImage']
            users = User.objects.all()
	    if  (select count(*) from User where username=newusername) > 0:
		return HttpResponse(newusername)
	    else:
	    	newuser = User()
           	newuser.username = newusername
                newuser.password = password
                newuser.headImage = headImage
                newuser.save()
                return HttpResponseRedirect('/VS/login')
        else:
            return False
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf': uf})

class UserFormforlogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


def login(request):
    if  request.method == 'POST':
        uf = UserFormforlogin(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            users = User.objects.all()
            if password  == users.get(username__exact=username).password:
                return HttpResponseRedirect('/VS/homepage')
            else:
                return HttpResponse('not ok')
    else:
        uf = UserFormforlogin()
    return render_to_response('login.html',{'uf': uf})
    

class UserFormforSubmitvideo(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    submitvideo = forms.FileField()

def submitvideo(request):
    if  request.method == 'POST':
        uf = UserFormforSubmitvideo(request.POST, request.FILES)
        if uf.is_valid():
            #print uf.cleaned_data['username']
            #print request.FILES
            #fp = file('upload/' + uf.cleaned_data['headImage'].name, 'wb')
            #s = uf.cleaned_data['headImage'].read()
            #fp.write(s)
            #fp.close()
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            submitvideo = uf.cleaned_data['submitvideo']
#            headImage = uf.cleaned_data['headImage']
            users = User.objects.all()
            if password  == users.get(username__exact=username).password:
                video = Video()
                video.entry = users.get(username__exact=username)
                video.videosource = submitvideo
                video.save()
                return HttpResponse('ok')
            else:
                return HttpResponse('not ok')
    else:
        uf = UserFormforSubmitvideo()
    return render_to_response('submitvideo.html',{'uf': uf})
   

def watchvideo(request):
    videos = Video.objects.all()
    videosource = videos[0].videosource
    return render_to_response('tempwatchvideo.html',{'videosource':videosource})


class UserFormforChangeinfo(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    newpassword = forms.CharField()


def changeinfo(request):
    if  request.method == 'POST':
        uf = UserFormforChangeinfo(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            newpassword = uf.cleaned_data['newpassword']
            users = User.objects.all()
            if password  == users.get(username__exact=username).password:
                userrr = users.get(username__exact=username)
                userrr.password = newpassword
                userrr.save()
                return HttpResponse('ok')
            else:
                return HttpResponse('not ok')
    else:
        uf = UserFormforChangeinfo()
    return render_to_response('changeinfo.html',{'uf': uf})


def homepage(req):
    return render_to_response('personalhomepage.html',{})

def searchForVideo(req):
    return render_to_response('searchVideo.html',{})

