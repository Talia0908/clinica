from django.shortcuts import render, redirect
from . models import Paciente, Medico, Medicamento
from . forms import PacienteForm

def home(request):
    return render (request, 'home.html')

def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render (request, 'paciente/list.html', {'pacientes': pacientes})

def paciente_show(request, id):
    return render (request, 'paciente/show.html', {'id': id})

def paciente_form(request):
    if (request.method == 'POST'):
        form = PacienteForm(request.POST)
        form.save()
        return redirect('/atendimento/paciente/')
    else:
        form = PacienteForm()
        return render(request,'paciente/form.html',{'form':form})

def medico_list(request):
    medicos = Medico.objects.all()
    return render (request, 'medico/list.html', {'medicos': medicos})

def medico_show(request, id):
    return render (request, 'medico/show.html', {'id': id})

def agendamento_list(request):
    return render (request, 'agendamento/list.html')

def medicamento_list(request):
    medicamentos = Medicamento.objects.all()
    return render (request, 'medicamento/list.html', {'medicamentos': medicamentos})
