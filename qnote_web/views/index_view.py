'''
Created by tklarryonline on Jun 06, 2014.
'''
from django.template.response import TemplateResponse
from django.views.generic.base import View
from qnote_api.models.quote import Quote


class IndexView(View):
    template = 'quotes/index.html'

    def get(self, request):
        context = {}
        context['quotes'] = Quote.objects.all()

        return TemplateResponse(request, self.template, context)