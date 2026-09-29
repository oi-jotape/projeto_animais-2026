from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('voluntariado/<int:pk>/inscrever/', views.volunteer_subscribe, name='volunteer_subscribe'),
    path('adocao/<int:pk>/solicitar/', views.animal_adopt, name='animal_adopt'),
    path('painel/', views.dashboard, name='dashboard'),
    path('painel/adocao/<int:pk>/status/<str:status>/', views.update_adoption_status, name='update_adoption_status'),
    path('painel/voluntario/<int:pk>/status/<str:status>/', views.update_volunteer_status, name='update_volunteer_status'),
]
