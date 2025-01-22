from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar o usuário
            user = form.get_user()
            login(request, user)
            messages.success(request, "Você foi logado com sucesso!")
            return redirect('home')  # Redirecionar para a página principal ou a página de destino
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Você pode fazer login agora.')
            return redirect('login')  # Redireciona para a página de login após o sucesso
        else:
            # Se o formulário não for válido, você pode adicionar um feedback para o usuário
            messages.error(request, 'Erro ao criar a conta. Verifique os dados e tente novamente.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)  # Essa função encerra a sessão do usuário
    return redirect('home')  # Redireciona para a página inicial ou qualquer página que você deseje