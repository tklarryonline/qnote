'''
Created by tklarryonline on May 21, 2014.
'''
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Quote(models.Model):
    user = models.ForeignKey(User)
    saying = models.TextField(_("Saying"))
    made_at = models.DateTimeField(_("Made at"))
    added_at = models.DateTimeField(_("Added at"))

    class Meta:
        app_label = "qnote_api"