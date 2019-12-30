from django.contrib.admin import ModelAdmin, register
from dtmult.propriedades.models import Propriedade


@register(Propriedade)
class PropriedadeAdmin(ModelAdmin):
    list_display = 'nome tipo_multipropriedade'.split()
    ordering = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}
