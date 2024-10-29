from tkinter.font import names

from django.urls import path
from . import views

#sao para onde eles sao redirecionados
urlpatterns = [
    path('', views.acesso, name='acesso'),
    path('formulario/', views.formulario, name='formulario'),
    path('processa_formulario/', views.processa_formulario, name ="processa_formulario"),
    path('pessoa/<int:pessoa_id>/', views.envio_formulario, name='envio_formulario'),
    path('lista/', views.PessoaList.as_view(), name='pessoa-lista'),
    path('update/<int:pk>/', views.PessoaUpdate.as_view(), name='pessoa-update'),
    path('detail/<int:pk>/', views.PessoaDetail.as_view(), name='pessoa-detail'),
    path('delete/<int:pk>/', views.delete_pessoa , name='pessoa-delete'),
    path('login/', views.login, name='login'),
]