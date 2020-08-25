from .models import DatosComentarios
from rest_framework import serializers

class DatosComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosComentarios
        fields = '__all__'