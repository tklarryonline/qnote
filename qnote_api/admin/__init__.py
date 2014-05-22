from django.contrib import admin
from qnote_api.admin.quote_admin import QuoteAdmin
from qnote_api.models.quote import Quote


admin.site.register(Quote, QuoteAdmin)