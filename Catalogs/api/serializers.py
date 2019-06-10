from rest_framework_mongoengine import serializers
from api.models import Cities, Schedules, CinemaRooms


class CitiesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Cities
        fields = '__all__'


class SchedulesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Schedules
        fields = '__all__'


class CinemaRoomsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CinemaRooms
        fields = '__all__'
