from django.shortcuts import render
from .service import notification
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from bson import json_util
from .serializers import *
import json
import datetime
from api.models import *


def getlist_user(request):
    if(request.method == 'GET'):
        list_user = Users.objects.all()
        list_user_srlz = UsersSerializer(list_user, many=True)
        return JsonResponse(list_user_srlz.data, safe=False)


@csrf_exempt
def add_user(request):
    #try:
    if(request.method == 'POST'):
        payload = json.loads(request.body)
        user = Users(
            username=payload['username'],
            password=payload['password'], 
            fullname=payload['fullname'],
            Email=payload['Email']
        )
        serU = UsersSerializer(data = user)
        if(serU.is_valid()):
            return JsonResponse({'statusCode':201,'message':'Valid Failed'}, safe=False)
        user.save()
        response = {'statusCode': 200,'message': 'Insert user successfully'}
    ##except BaseException as e:
     #   response = {'statusCode': 201, 'message': 'validation ERROR' + str(e)}
    return JsonResponse(response, safe=False)


def list_all(request):
    if(request.method == 'GET'):
        list_booking = Bookings.objects.all()
        list_booking_srlz = BookingsSerializer(list_booking, many=True)

        list_ticket = Tickets.objects.all()
        list_ticket_srlz = TicketsSerializer(list_ticket, many=True)

        return JsonResponse({'list_Booking': list_booking_srlz.data, 'list_Ticket': list_ticket_srlz.data}, safe=False)


@csrf_exempt
def order(request):
    if (request.method == 'POST'):

        payload = json.loads(request.body)
        try:
            user = Users.objects.get(pk=payload['UserID'])
        except:
            return JsonResponse({'statusCode': 201, 'message': 'user NOT FOUND'}, safe=False)

        try:
            booking = Bookings(
                UserID=user,
                Cinema=payload['Cinema'],
                Schedule=payload['Schedule'],
                Movie=payload['Movie'],
                Seat=payload['Seat'],
                TotalAmount=payload['TotalAmount']
            )
            booking.save()
            ticket = Tickets(
                Cinema=payload['Cinema'],
                Schedule=payload['Schedule'],
                Movie=payload['Movie'],
                Seat=payload['Seat'],
                Status='Paid',
                BookingID=booking
            )
            ticket.save()
            noti = {
                "Seat": payload['Seat'],
                "To": [user.Email],
                "Title": "Green Studio Cinema - Lich chieu phim" + payload['Movie'],
                "Content": "Lịch chiếu: " + payload['Schedule']
            }
            noti_res = notification.send_noti(noti)
        except BaseException as e:
            response = {'statusCode': 201, 'message': 'validation ERROR' + str(e)}
    return JsonResponse({'statusCode': 200, 'message': 'Order successfully!', 'noti_Result': noti_res}, safe=False)

@csrf_exempt
def update_user_by_ID (request):
    if (request.method == 'POST'):
        payload = json.loads(request.body)
        data = payload['data']
        user = Users.objects.get(pk = payload['id'])
        user_s = UsersSerializer(user,data = data)
        user_s.is_valid()
        user_s.save()   
        return JsonResponse(user_srlz.data,safe=False)