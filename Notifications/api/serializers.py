from rest_framework_mongoengine import serializers
from api.models import Notifications

class NotificationsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'