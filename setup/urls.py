from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from receitas.views import *

router = routers.DefaultRouter()
router.register('receitas', ReceitaViewSet, basename='receitas')
router.register('despesas', DespesaViewSet, basename='despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:ano>/<int:mes>', ReceitaAnoMesViewSet.as_view({"get": "list"})),
    path('despesas/<int:ano>/<int:mes>', DespesaAnoMesViewSet.as_view({"get": "list"})),
    path('resumo/<int:ano>/<int:mes>', ResumoViewSet.as_view())

]
