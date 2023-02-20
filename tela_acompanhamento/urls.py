from django.urls import path
from . import views

urlpatterns = [
  path('', views.acompanhamento, name='acompanhamento'),
  path('home/', views.voltarhome),
  path('<int:atendimentos_id>', views.ver_atendimento, name='ver_atendimento'),
]