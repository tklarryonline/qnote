'''
Created by tklarryonline on May 21, 2014.
'''
from django.http.response import HttpResponse
from common.json_serializer import JSONSerializer


def HttpJson(obj, status=200):
    return HttpResponse(JSONSerializer().serialize(obj, use_natural_keys=True),
                        content_type="application/json",
                        status=status)