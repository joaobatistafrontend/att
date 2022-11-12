from django.shortcuts import  render, redirect,HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def index(request):
    if request.method == 'GET':
        return render(request,'index.html')

def cadastro(request):
    if request.method == 'GET':
        return render (request,'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user:
            return HttpResponse('ja temos cadastro nesse nome')

        user = User.objects.create_user(username=username,password=password)
        user.save
        return HttpResponse('usuario cadastrado')


def logado(request):
    if request.method =='GET':
        return render (request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('plata')
        else:
            return HttpResponse('noa esta logado')

def desloga(request):
    if request.method =='GET':
        return render (request,'desloga.html')
    if request.method == 'POST':
        logout(request)
        return redirect('logando')
    else:
        return HttpResponse('usuario logado ainda')

def mudar_senha(request):
    if request.method =='GET':
        return render (request,'mudarsenha.html')
    if request.method == 'POST':
        logout(request)
        return redirect('logando')
    else:
        password = request.POST.get('password')

        user = User.objects.get(password=password)
        user.set_password
        user.save
        return redirect('pla')

def plataforma(request):
    if request.user.is_authenticated:
        return render(request,'plataforma.html')
    else:
        return HttpResponse('precisa logar')
