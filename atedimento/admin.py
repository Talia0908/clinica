from django.contrib import admin

from . models import Paciente
from . models import Medico

admin.site.register(Paciente)
admin.site.register(Medico)

