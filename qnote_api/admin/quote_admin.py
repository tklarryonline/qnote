'''
Created by tklarryonline on May 23, 2014.
'''
from django.contrib.admin import ModelAdmin


class QuoteAdmin(ModelAdmin):
    list_display = ('id', 'user', 'saying', 'made_at', 'added_at')