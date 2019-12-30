import pytest
from django.urls import reverse
from model_mommy import mommy

from dtmult.django_assertions import assert_contains
from dtmult.propriedades.models import Propriedade


@pytest.fixture
def propriedade(db):
    return mommy.make(Propriedade)


@pytest.fixture
def resp(client, propriedade):
    return client.get(reverse('propriedades:propriedade', args=(propriedade.slug,)))


@pytest.fixture
def resp_prop_nao_encontrado(client, propriedade):
    return client.get(reverse('propriedades:propriedade', args=(propriedade.slug + 'propriedade_nao_existente',)))


def test_status_code_prop_nao_encontrado(resp_prop_nao_encontrado):
    assert resp_prop_nao_encontrado.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_prop(resp, propriedade):
    assert_contains(resp, propriedade.nome)


# def test_conteudo_prop(resp, video):
#     assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')
