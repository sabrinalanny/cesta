from rest_framework.routers import DefaultRouter
from api.views import FuncionarioViewSet, EmpresaViewSet, CestaViewSet, FuncionarioCestaViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'funcionario', FuncionarioViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'cesta', CestaViewSet)
router.register(r'funcionariocesta', FuncionarioCestaViewSet)

urlpatterns = router.urls