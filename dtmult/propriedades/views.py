from django.shortcuts import get_object_or_404, render

from dtmult.propriedades.models import Propriedade


def indice(request):
    propriedades = Propriedade.objects.order_by('nome').all()
    return render(request, 'propriedades/indice.html', context={'propriedades': propriedades})


def propriedade(request, slug):
    propriedade = get_object_or_404(Propriedade, slug=slug)
    return render(request, 'propriedades/propriedade.html', context={'propriedade': propriedade})
