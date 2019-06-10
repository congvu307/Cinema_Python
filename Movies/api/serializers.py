from rest_framework_mongoengine import serializers
from api.models import Movies

class MoviesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Movies
        fields = '__all__'