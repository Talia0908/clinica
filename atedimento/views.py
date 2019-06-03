from django.shortcuts import render

def home(request):
    return render(request,'home.html') 

def paciente_list(request):
    return render(request,'paciente/list.html') 

def paciente_show(request, id):
    return render(request, 'paciente/show.html', {'id': id}) 


def medico_list(request):
    return render(request,'medico/list.html')

def medico_show(request, id):
    return render(request, 'medico/show.html', {'id': id})

def agendamento_list(request):
    return render(request, 'agendamento/list.html')
    