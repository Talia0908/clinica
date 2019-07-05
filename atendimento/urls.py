from django.urls import path

from . import views

urlpatterns = [
    path('',views.home),
    path('paciente/', views.paciente_list),
    path('paciente/<int:id>/', views.paciente_show),
    path('medico/', views.medico_list),
    path('medico/<int:id>/', views.medico_show),
    path('agendamento/', views.agendamento_list),
    path('medicamento/', views.medicamento_list),
    path('paciente/create/', views.paciente_form),\
]