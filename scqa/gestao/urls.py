from django.urls import path

from gestao import views

urlpatterns = [
    path('registros-entrada', views.registro_entrada_list, name='registro_entrada_list'),
    path('novo-registro-entrada', views.registro_entrada_create, name='registro_entrada_create'),
    path('ver-registro-entrada/<str:pk>/', views.registro_entrada_read, name='registro_entrada_read'),

]
