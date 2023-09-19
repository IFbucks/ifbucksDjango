import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from ifbucks.views import (
    CategoriaViewSet,
    UsuarioViewSet,
    PedidoViewSet,
    ProdutoViewSet,
    ItemPedidoViewSet,
    MesaViewSet,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"usuarios", UsuarioViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"itempedidos", ItemPedidoViewSet)
router.register(r"mesas", MesaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include((router.urls, "api"))),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# Servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
