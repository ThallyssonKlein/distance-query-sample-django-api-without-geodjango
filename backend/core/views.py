from django.shortcuts import render

from .models import Loja

from django.http import HttpResponse

import math
import decimal
from django.forms.models import model_to_dict
import json
from django.core import serializers

def calcDistance(lat1, lon1, lat2, lon2):
    print(lat1, lon1, lat2, lon2)
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def queryLojas(request):
    queryset = Loja.objects.all()
    long = math.radians(float(request.GET.get('long')))
    lat = math.radians(float(request.GET.get('lat')))
    distances = []
    names = {}
    for i, loja in enumerate(queryset):
        distance = calcDistance(lat, long, math.radians(loja.latitude), math.radians(loja.longitude))
        distances.append(distance)
        names[loja.id] = distance
    distances.sort()
    lojasList = []
    # for loja in queryset:
    #     for n in names.keys():
    #         if n == loja.id:
    #             lojasList.append({
    #                 'distance' : names[n],
    #                 'loja' : json.loads(serializers.serialize('json', [loja]))
    #             })
    for d in distances:
        for n in names.items():
            if n[1] == d:
               loja = queryset.get(id=n[0])
               serializedJson = json.loads(serializers.serialize('json', [loja]))
               fields = serializedJson[0].get('fields')
               fields['id'] = serializedJson[0].get('pk')
               lojasList.append(fields) 
    return HttpResponse(json.dumps(lojasList), content_type='application/json')
def index(request):
    return HttpResponse('Ok')
    
