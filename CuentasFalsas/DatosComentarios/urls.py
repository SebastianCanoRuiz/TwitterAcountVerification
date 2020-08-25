from rest_framework import routers
from django.urls import path
from .viewsets import DatosComentariosViewSet

router = routers.SimpleRouter()
router.register('DatosComentarios', DatosComentariosViewSet)

urlpatterns = router.urls