from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('listar_alunos', views.listar_alunos, name='listar_alunos'),
    path('detalhar_aluno/<int:id>', views.detalhar_aluno, name='detalhar_aluno'),
    path('cadastrar_aluno', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alterar_aluno/<int:id>', views.alterar_aluno, name='alterar_aluno'),
    path('excluir_aluno/<int:id>', views.excluir_aluno, name='excluir_aluno'),
    # permitir o fluxo de login
    path('login/', views.login_view, name='login'),
    # permitir o fluxo de login
    path('logout/', views.logout_view, name='logout'), 
    # permitir o cadastro de um novo usuário
    path('register/', views.register_view, name='register'),
]