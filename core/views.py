from django.shortcuts import  render, redirect,HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View,CreateView,TemplateView,UpdateView

class Index(TemplateView):
    template_name = 'index.html'


class Cadastro(CreateView):
    def get(self,request):
        return render(request,'cadastro.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user:
            return HttpResponse('ja temos cadastro nesse nome')

        user = User.objects.create_user(username=username,password=password)
        user.save
        return HttpResponse('usuario cadastrado')        


class Logado(View):
    def get(self,request):
        return render(request,'login.html')  

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('pla')
        else:
            return HttpResponse('noa esta logado')        



class Desloga(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render (request,'desloga.html')   

    def post(self,request):
        if request.method == 'POST':
            logout(request)
            return HttpResponse('usuario deslogado')
        else:
            return HttpResponse('usuario logado ainda')



class Senha(UpdateView):
    def get(self,request):
        if request.user.is_authenticated:
            return render (request,'senha.html') 

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        if user:
            user.set_password(password)   
            user.save()
            return redirect('pla')


def mudar_senha(request):
    if request.method =='GET':
        return render (request,'mudarsenha.html')
    if request.method == 'POST':
        logout(request)
        return redirect('logando')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.get(username=username)
        user.set_password(password)
        user.save
        return redirect('pla')

def plataforma(request):
    if request.user.is_authenticated:
        return render(request,'plataforma.html')
    else:
        return HttpResponse('precisa logar')
