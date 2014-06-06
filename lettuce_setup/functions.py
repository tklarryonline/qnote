'''
Created by tklarryonline on Jun 06, 2014.
'''
import urlparse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from lettuce import world, before
from lettuce_setup.selenium_shortcuts import browser


def default_user(number=1):
    if number in world.users:
        return world.users[number]

    try:
        user = User.objects.create_user(
            'username%s' % number,
            'luan+testqnote%s@tklarryonline.me' % number,
            'password'
        )
    except:
        user = User.objects.get_by_natural_key('username%s' % number)

    user.raw_password = 'password'
    world.users[number] = user
    return user


@before.each_scenario
def clear_user(scenario):
    User.objects.all().delete()
    world.users = {}


def django_url(url='', host='localhost'):
    base_url = 'http://%s' % host

    port = getattr(settings, 'LETTUCE_SERVER_PORT', 8000)
    if port is not 80:
        base_url += ':%d' % port

    return urlparse.urljoin(base=base_url, url=url)


def visit(url):
    browser().get(django_url(url))
    
    
def visit_by_view_name(name, **kwargs):
    visit(reverse(name, **kwargs))
