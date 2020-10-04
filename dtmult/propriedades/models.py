from django.db import models
from django.urls import reverse
from dtmult.base.models import User
from ordered_model.models import OrderedModel


class TipoMultiPropriedade(OrderedModel):
    nome = models.CharField(max_length=32, blank=False, null=False, unique=True)
    descricao = models.CharField(max_length=100, null=True)
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        verbose_name = 'Tipo de Multipropriedade'
        verbose_name_plural = 'Tipos de Multipropriedades'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('propriedades:detalhe', kwargs={'slug': self.slug})


class Propriedade(OrderedModel):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    comentarios = models.TextField()
    slug = models.SlugField(max_length=32, unique=True)
    foto = models.ImageField(upload_to='img/propriedades/', null=True, blank=True)
    multiproprietarios = models.ManyToManyField(User)
    tags = models.CharField(max_length=200)
    tipo_multipropriedade = models.ForeignKey('TipoMultiPropriedade', on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    order_with_respect_to = 'tipo_multipropriedade'

    class Meta(OrderedModel.Meta):
        verbose_name_plural = "Propriedades"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('propriedades:propriedade', kwargs={'slug': self.slug})
