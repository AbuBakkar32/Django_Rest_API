import json
from django.http import JsonResponse

from django.shortcuts import render


# Create your views here.
def api_view(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)
