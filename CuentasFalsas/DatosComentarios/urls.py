from rest_framework import routers
from django.conf.urls import url
from .viewsets import DatosComentariosViewSet

router = routers.SimpleRouter()
router.register('DatosComentarios', DatosComentariosViewSet)

urlpatterns = [
    path('coment/', DatosComentariosViewSet),
]
#urlpatterns = router.urls