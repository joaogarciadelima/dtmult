from dtmult.propriedades.views import indice_multipropriedade


def listar_tipos_multipropriedades(request):
    return {'TIPOMULTIPROPRIEDADE': indice_multipropriedade()}
