'''
Created by tklarryonline on May 21, 2014.
'''
from django.views.generic.base import View
from common.django_custom import HttpJson
from qnote_api.models.quote import Quote


class QuoteView(View):
    def get(self, request):
        data = {}
        quotes = Quote.objects.all()
        data['quotes'] = quotes

        return HttpJson(data)