from django.contrib.admin import register
from ordered_model.admin import OrderedModelAdmin

from dtmult.propriedades.models import Propriedade, TipoMultiPropriedade


@register(TipoMultiPropriedade)
class TipoMultiPropriedadeAdmin(OrderedModelAdmin):
    list_display = 'nome move_up_down_links'.split()
    prepopulated_fields = {'slug': ('nome',)}


@register(Propriedade)
class PropriedadeAdmin(OrderedModelAdmin):
    list_display = ('nome', 'tipo_multipropriedade', 'order', 'move_up_down_links')
    list_filter = ('tipo_multipropriedade',)
    ordering = ('tipo_multipropriedade', 'order')
    prepopulated_fields = {'slug': ('nome',)}
