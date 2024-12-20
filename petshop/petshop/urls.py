"""
URL configuration for petshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from cliente.api.views import ClienteViewSet
from animais.api.views import AnimalViewSet
from produto.api.views import ProdutoViewSet, VendaViewSet
from servicoPet.api.views import ServicoPetViewSet

router = SimpleRouter()

router.register("Cliente", ClienteViewSet, basename="Clientes")
router.register("Animal", AnimalViewSet, basename="animais")
router.register("ServicoPet", ServicoPetViewSet, basename="ServicosPet")
router.register("Produto", ProdutoViewSet, basename="Produtos")
router.register("Venda", VendaViewSet, basename="Vendas")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+router.urls
