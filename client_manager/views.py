from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from .models import Manager, Client


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/profile')
                else:
                    return render(request, 'login.html',
                                  {'form': form, 'error_msg': 'Аккаунт отключен'})
            else:
                return render(request, 'login.html',
                              {'form': form, 'error_msg': 'Неправильный логин или пароль'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], password=cd['password'])
            manager = Manager(name=cd['name'], user=user, login=cd['username'], password=cd['password'])
            manager.save()
            return redirect('/login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def view_profile(request):
    if request.method == 'GET':
        manager = Manager.objects.get(user=request.user)
        clients = Client.objects.all().filter(employer=manager)
        return render(request, 'profile.html', {'clients': clients})
    elif request.method == 'POST':
        manager = Manager.objects.get(user=request.user)
        clients = list(Client.objects.all().filter(employer=manager))
        clients[int(request.POST['id_client'])].status = request.POST['new_status']
        clients[int(request.POST['id_client'])].save()
        return HttpResponse(status=200)
