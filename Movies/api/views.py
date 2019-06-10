from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson import json_util
from .serializers import MoviesSerializer
import json
import datetime
from api.models import Movies


def get_premiere(request):
    if (request.method == 'GET'):
        now = datetime.datetime.now()
        print(now.year)
        list_premieres = Movies.objects(
            ReleaseYear__gt = (now.year - 1),
            ReleaseYear__lte = now.year,
            ReleaseMonth__gte = now.month,
            ReleaseMonth__lte = (now.month + 2),
            ReleaseDay__lte = now.day
        )
        lisr_premieres_srlz = MoviesSerializer(list_premieres,many=True)
        return JsonResponse(lisr_premieres_srlz.data, safe=False)

def get_list(request):
    try:
        if (request.method == 'GET'):
            list_Movies = Movies.objects.all()
            Movies_srlz = MoviesSerializer(list_Movies, many=True)
            return JsonResponse(Movies_srlz.data, safe=False)
        else:
            return JsonResponse({'statusCode': 404, 'message': 'Wrong method!'}, safe=False)
    except:
        return JsonResponse({'statusCode': 404, 'message': 'Get list error!'}, safe=False)


@csrf_exempt
def add_movie(request):
    if (request.method == 'POST'):
        payload = json.loads(request.body)
        print(payload['Title'])

        movie = Movies(
            Title=payload['Title'],
            Runtime=payload['Runtime'],
            Format=payload['Format'],
            Plot=payload['Plot'],
            ReleaseYear=payload['ReleaseYear'],
            ReleaseMonth=payload['ReleaseMonth'],
            ReleaseDay=payload['ReleaseDay'],
        )
        try:
            movie.save()
            response = {'statusCode': 200, 'message': 'Insert successfully!'}
        except:
            response = {'statusCode': 201, 'message': 'Insert failed!'}
    return JsonResponse(response, safe=False)

# Create your views here
