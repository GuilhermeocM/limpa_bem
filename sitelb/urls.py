from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('intranet/', views.intranet),
    path('cadastro/', views.cadastro),
]