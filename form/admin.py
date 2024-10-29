from django.contrib import admin

# Register your models here.

from .models import Pessoa, Contato, Experiencia, Formacao

admin.site.register(Pessoa)
admin.site.register(Contato)
admin.site.register(Experiencia)
admin.site.register(Formacao)