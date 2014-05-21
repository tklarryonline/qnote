'''
Created by tklarryonline on May 22, 2014.
'''
import factory
from django.contrib.auth.models import User
from common.tests.factories import fake


class UserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = User

    username = factory.LazyAttribute(lambda n: fake.user_name())
    password = 'password'
    is_superuser = True
    is_staff = True
    is_active = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.raw_password = password
            user.set_password(password)
            if create:
                user.save()
        return user