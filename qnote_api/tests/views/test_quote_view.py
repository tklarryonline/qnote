'''
Created by tklarryonline on May 21, 2014.
'''
import json
import sure
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from qnote_api.models.quote import Quote


class QuoteViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_quotes(self):
        response = self.client.get(reverse('qnote_api_quotes'))

        response.status_code.should.equal(200)

        quotes = json.loads(response.content)['quotes']
        system_quotes_count = Quote.objects.all().count()
        len(quotes).should.equal(system_quotes_count)