from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from models import diary_contents

# Create your views here.\
def main(request):
    contents = diary_contents.objects.all()
    return render_to_response('index.html', RequestContext(request, {"contents" : contents}))


def login_call(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')

        else:
             return HttpResponse('disabled account')

    else:
            return HttpResponse('invalid login')

def register_call(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, password, email)
    user.save()

    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')

        else:
            return HttpResponse('disabled account')

    else:
        return HttpResponse('invalid login')

def logout_call(request):
    logout(request)
    return redirect('/')
