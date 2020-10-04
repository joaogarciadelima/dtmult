import pytest
from django.urls import reverse
from model_mommy import mommy

from dtmult.django_assertions import assert_contains
from dtmult.propriedades.models import TipoMultiPropriedade, Propriedade


@pytest.fixture
def tipo_multipropriedade(db):
    return mommy.make(TipoMultiPropriedade)


@pytest.fixture
def propriedades(tipo_multipropriedade):
    return mommy.make(Propriedade, 2, tipo_multipropriedade=tipo_multipropriedade)


@pytest.fixture
def resp(client, tipo_multipropriedade, propriedades):
    resp = client.get(reverse('propriedades:detalhe', kwargs={'slug': tipo_multipropriedade.slug}))
    return resp


def test_nomes(resp, tipo_multipropriedade: TipoMultiPropriedade):
    assert_contains(resp, tipo_multipropriedade.nome)


def test_descricao(resp, tipo_multipropriedade: TipoMultiPropriedade):
    assert_contains(resp, tipo_multipropriedade.descricao)


def test_propriedades_nomes(resp, propriedades):
    for propriedade in propriedades:
        assert_contains(resp, propriedade.nome)
