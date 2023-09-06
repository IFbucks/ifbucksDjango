from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import os
from ifbucks.views import (
    CategoriaViewSet,
    TipoPessoaViewSet,
    UsuarioViewSet,
    PedidoViewSet,
    TipoProdutoViewSet,
    ProdutoViewSet,
    ItemPedidoViewSet,
)

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'tipopessoas', TipoPessoaViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'tipoprodutos', TipoProdutoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'itempedidos', ItemPedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include((router.urls, 'api'))),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)