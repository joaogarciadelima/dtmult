import pytest
from django.urls import reverse
from model_mommy import mommy

from dtmult.django_assertions import assert_contains
from dtmult.propriedades.models import TipoMultiPropriedade


@pytest.fixture
def tipos_multipropriedades(db):
    return mommy.make(TipoMultiPropriedade, 2)


@pytest.fixture
def resp(client, tipos_multipropriedades):
    resp = client.get(reverse('base:home'))
    return resp


def test_nomes(resp, tipos_multipropriedades):
    for tipo_multipropriedade in tipos_multipropriedades:
        assert_contains(resp, tipo_multipropriedade.nome)
