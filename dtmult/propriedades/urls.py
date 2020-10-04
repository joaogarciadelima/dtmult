from django.urls import path

# from dtmult.propriedades.views import detalhe, propriedade, propriedade_list, propriedade_detail,\
#     PropriedadeViewSet, indice_multipropriedade
from dtmult.propriedades.views import detalhe, propriedade

app_name = 'propriedades'

# router = routers.DefaultRouter()
# router.register(r'api', PropriedadeViewSet)


urlpatterns = [
    path('', propriedade, name='propriedade'),
    path('<slug:slug>', detalhe, name='detalhe'),
    # path('<slug:slug>', indice_multipropriedade, name='indice'),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('propri/', propriedade_list),
    # path('propriedades/<int:pk>/', propriedade_detail),
]
