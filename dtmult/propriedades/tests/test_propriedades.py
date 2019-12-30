import pytest
from django.urls import reverse
from model_mommy import mommy

from dtmult.django_assertions import assert_contains
from dtmult.propriedades.models import Propriedade


@pytest.fixture
def propriedades(db):
    return mommy.make(Propriedade, 3)


@pytest.fixture
def resp(client, propriedades):
    return client.get(reverse('propriedades:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_nome_propriedade(resp, propriedades):
    for propriedade in propriedades:
        assert_contains(resp, propriedade.nome)


# def test_link_video(resp, propriedades):
#     for propriedade in propriedades:
#         video_link = reverse('aperitivos:video', args=(video.slug,))
#         assert_contains(resp, f'href="{video_link}"')
