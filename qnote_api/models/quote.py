'''
Created by tklarryonline on May 21, 2014.
'''
from django.db import models


class Quote(models.Model):

    class Meta:
        app_label = "qnote_api"