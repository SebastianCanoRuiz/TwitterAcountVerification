from rest_framework import viewsets

from .models import DatosComentarios
from .serializer import DatosComentariosSerializer

class DatosComentariosViewSet(viewsets.ModelViewSet):
    queryset = DatosComentarios.objects.all()
    serializer_class = DatosComentariosSerializer