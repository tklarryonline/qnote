'''
Created by tklarryonline on May 22, 2014.
'''
import factory
from common.tests.factories import fake
from common.tests.factories.user_factory import UserFactory
from qnote_api.models.quote import Quote


class QuoteFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Quote

    user = factory.SubFactory(UserFactory)
    saying = factory.LazyAttribute(lambda n: fake.paragraph(nb_sentences=3))
    made_at = factory.LazyAttribute(lambda n: fake.date_time_this_century())
    added_at = factory.LazyAttribute(lambda n: fake.date_time_this_month())