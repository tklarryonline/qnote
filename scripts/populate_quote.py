'''
Created by tklarryonline on May 23, 2014.
'''
from django.contrib.auth.models import User
from qnote_api.tests.factories.quote_factory import QuoteFactory


user = User.objects.all().first()
for i in range(0, 100):
    QuoteFactory(user=user)