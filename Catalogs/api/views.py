from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson import json_util
from .serializers import CitiesSerializer, CinemaRoomsSerializer, SchedulesSerializer
import json
import datetime
from api.models import Schedules, CinemaRooms, Cities


def getlist_city(request):
    try:
        if (request.method == 'GET'):
            list_Cities = Cities.objects.all()
            Movies_srlz = CitiesSerializer(list_Cities, many=True)
            return JsonResponse(Movies_srlz.data, safe=False)
        else:
            return JsonResponse({'statusCode': 404, 'message': 'Wrong method!'}, safe=False)
    except:
        return JsonResponse({'statusCode': 404, 'message': 'Get list error!'}, safe=False)


@csrf_exempt
def add_city(request):
    if (request.method == 'POST'):
        payload = json.loads(request.body)
        city = Cities(
            name=payload['name']
        )
        try:
            city.save()
            response = {'statusCode': 200, 'message': 'Insert successfully!'}
        except:
            response = {'statusCode': 201, 'message': 'Insert failed!'}
    return JsonResponse(response, safe=False)


def getlist_cinemaRoom(request):
    try:
        if (request.method == 'GET'):
            list_cinemaRooms = CinemaRooms.objects.all()
            CinemaRoom_srlz = CinemaRoomsSerializer(
                list_cinemaRooms, many=True)
            return JsonResponse(CinemaRoom_srlz.data, safe=False)
        else:
            return JsonResponse({'statusCode': 404, 'message': 'Wrong method!'}, safe=False)
    except:
        return JsonResponse({'statusCode': 404, 'message': 'Get list error!'}, safe=False)


@csrf_exempt
def add_cinemaRoom(request):
    if (request.method == 'POST'):
        payload = json.loads(request.body)
        try:
            city = Cities.objects.get(pk=payload['CityID'])
        except:
            return JsonResponse({'statusCode': 201, 'message': 'City not found!'}, safe=False)

        cinemaRoom = CinemaRooms(
            CityID=city,
            Location=payload['Location'],
            Name=payload['Name'],
            Capacity=payload['Capacity'],
            Type=payload['Type'],
            Flot=payload['Flot'],
        )
        cinemaRoom.save()
        response = {'statusCode': 200, 'message': 'Insert successfully!'}
        # except:
        #     response = {'statusCode': 201, 'message': 'Insert failed!'}
        #cz = CitiesSerializer(city)
    return JsonResponse(response, safe=False)


@csrf_exempt
def add_schedule(request):
    if (request.method == 'POST'):
        payload = json.loads(request.body)
        try:
            cinemaRoom = CinemaRooms.objects.get(pk=payload['CinemaRoomID'])
        except:
            return JsonResponse({'statusCode': 201, 'message': 'City not found!'}, safe=False)

        schedule = Schedules(
            Time=payload['Time'],
            CinemaRoomID=cinemaRoom,
            seatsEmpty=payload['seatsEmpty'],
            seatsOccupied=payload['seatsOccupied'],
            price=payload['price'],
            MovieID=payload['MovieID'],
        )
        schedule.save()
        response = {'statusCode': 200, 'message': 'Insert successfully!'}
        # except:
        #     response = {'statusCode': 201, 'message': 'Insert failed!'}
        #cz = CitiesSerializer(city)
    return JsonResponse(response, safe=False)


def schedule_by_movieID(request, movie_ID):
    if (request.method == 'GET'):
        print(movie_ID)
        schedule = Schedules.objects(MovieID=movie_ID)
        schedule_srlz = SchedulesSerializer(schedule, many=True)
        print(schedule)
        return JsonResponse(schedule_srlz.data, safe=False)


def getlist_schedule(request):
    if (request.method == 'GET'):
        list_schedule = Schedules.objects.all()
        schedule_srlz = SchedulesSerializer(list_schedule, many=True)
        return JsonResponse(schedule_srlz.data, safe=False)
