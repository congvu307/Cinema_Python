from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from bson import json_util
from .serializers import NotificationsSerializer
import json
import datetime
from api.models import Notifications


def getlist_noti(request):
    if (request.method == 'GET'):
        list_noti = Notifications.objects.all()
        list_noti_srlz = NotificationsSerializer(list_noti, many=True)
        return JsonResponse(list_noti_srlz.data, safe=False)


@csrf_exempt
def add_noti(request):
    if(request.method == 'POST'):
        payload = json.loads(request.body)
        print(payload)
        try:
            send_mail(payload['Title'], payload['Content'],
                    settings.EMAIL_HOST_USER, payload['To'], fail_silently=False)
            noti = Notifications(
                Type='Email',
                Title=payload['Title'],
                Content=payload['Content'],
                From=settings.EMAIL_HOST_USER,
                Seat=payload['Seat'],
                To=payload['To']
            )
            noti.save()
            response = {'statusCode': 200,'message': 'Push notification successfully!'}
        except:
             response = {'statusCode': 201,'message': 'Push notification FAILED'}
        return JsonResponse(response, safe=False)
