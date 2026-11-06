from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Aluno
from .forms import AlunoForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
        return render(request, 'alunos/index.html', {})

def sobre(request):
        return render(request, 'alunos/sobre.html', {'nome_projeto': 'Universidade'})

@login_required(login_url='login')
def listar_alunos(request):
        alunos = Aluno.objects.all()
        return render(request, 'alunos/listar_alunos.html', {'alunos': alunos})

@login_required(login_url='login')
def detalhar_aluno(request, id):
        aluno = None
        try:
                aluno = Aluno.objects.get(pk=id)
        except:
                pass
        return render(request, 'alunos/detalhar_aluno.html', {'aluno': aluno})

@login_required(login_url='login')
def cadastrar_aluno(request):
        if request.POST:
                form = AlunoForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request, "Aluno cadastrado com sucesso.")
                        return redirect('listar_alunos')
                messages.error(request, "Erro no preenchimento do formulário.")
                return render(request, 'alunos/form_aluno.html', {'form': form})
        form = AlunoForm()
        return render(request, 'alunos/form_aluno.html', {'form': form})

@login_required(login_url='login')
def alterar_aluno(request, id):
        aluno = Aluno.objects.get(pk=id)
        if request.POST:
                form = AlunoForm(request.POST, instance=aluno)
                if form.is_valid():
                        form.save()
                        messages.success(request, "Aluno alterado com sucesso.")
                        return redirect('listar_alunos')
                messages.error(request, "Erro no preenchimento do formulário.")
                return render(request, 'alunos/form_aluno.html', {'form': form, 'editar': True})
        form = AlunoForm(instance=aluno)
        return render(request, 'alunos/form_aluno.html', {'form': form, 'editar': True})

@login_required(login_url='login')
def excluir_aluno(request, id):
        aluno = Aluno.objects.get(pk=id)
        if request.POST:
                aluno.delete()
                messages.success(request, "Aluno deletado com sucesso.")
                return redirect('listar_alunos')
        return render(request, 'alunos/excluir_aluno.html', {'aluno': aluno})

# Página de registro
def register_view(request):
        password = None
        if request.method == "POST":
                # Valores informados no cadastro
                username = request.POST['username']
                password = request.POST['password']
                confirm_password = request.POST['confirm_password']

        if password is not None and password == confirm_password:
                # Inclusão no banco de dados do novo usuário
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, "Usuário criado com sucesso!")
                return redirect('login')
        else:
                messages.error(request, "As senhas não conferem!")

        return render(request, 'register.html')


# Página de login
def login_view(request):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                # Método para verificar as credenciais
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user) # cria a sessão
                        return redirect('listar_alunos')
                else:
                        messages.error(request, "Usuário ou senha inválidos!")
        return render(request, 'login.html')

# Página de logout
def logout_view(request):
        logout(request)
        return redirect('login')