# sourceimport os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from ifbucks.views import (
    CategoriaViewSet,
    UsuarioViewSet,
    PedidoViewSet,
    ProdutoViewSet,
    CarrinhoViewSet,
    MesaViewSet,
    PedidosMesa,
    CarrinhoMesa,
    ProdutosCategoria,
)

router = DefaultRouter()
router.register("categorias", CategoriaViewSet, basename="Categorias")
router.register("usuarios", UsuarioViewSet, basename="Usuarios")
router.register("pedidos", PedidoViewSet, basename="Pedidos")
router.register("produtos", ProdutoViewSet, basename="Produtos")
router.register("carrinho", CarrinhoViewSet, basename="Carrinho")
router.register("mesas", MesaViewSet, basename="Mesas")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("mesas/<int:pk>/pedidos/", PedidosMesa.as_view(), name="pedidos-mesa"),
    path("mesas/<int:pk>/carrinho/", CarrinhoMesa.as_view(), name="carrinho-mesa"),
    path(
        "categorias/<str:pk>/produtos/",
        ProdutosCategoria.as_view(),
        name="produtos-categoria",
    ),
    path("api/media/", include(uploader_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/validate/", TokenVerifyView.as_view(), name="token_verify"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)