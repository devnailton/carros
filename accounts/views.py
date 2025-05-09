
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #UserCreationForm já vem com o Django, lá do admin, e AuthenticationForm é para validação de login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, request.FILES) #O UserCreationForm já faz a validação das senhas iguais
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm() #variável que recebe uma instância do UserCreationForm
    return render( #retorna para o usuário um template, com os dados do formulário
        request,
        'register.html',
        {'user_form': user_form} 
    )

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('login')