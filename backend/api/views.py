from django.shortcuts import render
from django.http import JsonResponse

import json

def api_home(request, *args, **kwargs):

    print(request.GET, " get") # will give query params from get request || backend side
    print(request.POST, " post") # will give query params from post request || backend side

    body = request.body
    data = {} # || used in the client -> it is what json is returning
    try:
        data = json.loads(body) # takes a string of json and turns it into a dictionary
    except Exception:
        pass
    
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type


    return JsonResponse(data) 