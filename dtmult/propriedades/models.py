from django.db import models
from django.urls import reverse
from dtmult.base.models import User


class Propriedade(models.Model):
    class Meta:
        verbose_name_plural = "Propriedades"

    tipos_multipropriedades = [
        ('IM', 'Imóvel'), ('VE', 'Veículo')
    ]
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    comentarios = models.TextField()
    slug = models.SlugField(max_length=32, unique=True)
    foto = models.ImageField(upload_to="img/propriedades/", null=True, blank=True)
    multiproprietarios = models.ManyToManyField(User)
    tags = models.CharField(max_length=200)
    tipo_multipropriedade = models.CharField(max_length=2, choices=tipos_multipropriedades)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    # writer = models.ForeignKey(User.id, on_delete=models.CASCADE)

    def __str__(self):
        return f'Propriedade: {self.nome}'

    def get_absolute_url(self):
        return reverse('propriedades:propriedade', args=(self.slug,))
