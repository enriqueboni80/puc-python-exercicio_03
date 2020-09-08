from django.contrib import admin
from .models.pessoa import Pessoa
from .models.departamento import Departamento

admin.site.register(Pessoa)
admin.site.register(Departamento)
