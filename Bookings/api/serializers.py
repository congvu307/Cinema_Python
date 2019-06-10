from rest_framework_mongoengine import serializers
from api.models import Bookings, Tickets, Users


class BookingsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'


class TicketsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'


class UsersSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Users
        fields = '__all__'
