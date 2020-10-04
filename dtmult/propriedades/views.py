# from django.http import JsonResponse, HttpResponse
# from rest_framework import viewsets
# from rest_framework.parsers import JSONParser
from typing import List

# from .serializers import PropriedadeSerializer

from django.shortcuts import get_object_or_404, render

from dtmult.propriedades.models import Propriedade, TipoMultiPropriedade


def indice(request):
    propriedades = Propriedade.objects.order_by('order').all()
    return render(request, 'propriedades/indice.html', context={'propriedades': propriedades})


def propriedade(request, slug):
    propriedade = get_object_or_404(Propriedade, slug=slug)
    return render(request, 'propriedades/propriedade.html', context={'propriedade': propriedade})


def encontrar_tipo_multipropriedade(slug: str) -> TipoMultiPropriedade:
    return TipoMultiPropriedade.objects.get(slug=slug)


def listar_propriedades_tipo_ordenadas(tipo_multipropriedades: TipoMultiPropriedade):
    return list(tipo_multipropriedades.propriedade_set.order_by('order').all())


def detalhe(request, slug):
    detalhe = encontrar_tipo_multipropriedade(slug)
    propriedades = listar_propriedades_tipo_ordenadas(detalhe)
    return render(request, 'propriedades/detalhe.html', {'propriedades': detalhe}, {'propriedades': propriedades})


def indice_multipropriedade() -> List[TipoMultiPropriedade]:
    """
    Lista tipos de multipropriedades ordenadas por nome
    :return:
    """
    return list(TipoMultiPropriedade.objects.order_by('order').all())


# def propriedade_list(request):
#     """
#     Retorna todas as propriedades
#     :param request:
#     :return:
#     """
#     if request.method == "GET":
#         rest_list = Propriedade.objects.order_by('order').all()
#         serializer = PropriedadeSerializer(rest_list, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PropriedadeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# def propriedade_detail(request, pk):
#     """
#     Retorna, atualiza ou deleta uma propriedade
#     :param request:
#     :param pk:
#     :return:
#     """
#     try:
#         propriedade = Propriedade.objects.get(pk=pk)
#     except Propriedade.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == "GET":
#         rest_list = Propriedade.objects.order_by('data_cadastro').all()
#         serializer = PropriedadeSerializer(rest_list, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PropriedadeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         propriedade.delete()
#         return HttpResponse(status=204)
#
#
# class PropriedadeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows properties to be viewed or edited.
#     """
#     queryset = Propriedade.objects.all()
#     serializer_class = PropriedadeSerializer
