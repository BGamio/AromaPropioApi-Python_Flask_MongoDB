from rest_framework import serializers
from Api.models import Post, Resennia, LibroDeReclamaciones

class PostSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ResenniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resennia
        fields = '__all__'

class LibroDeReclamacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDeReclamaciones
        fields = '__all__'