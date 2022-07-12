from django.contrib import admin
from main.models import *
from modeltranslation.translator import translator,TranslationOptions

# Register your models here.

admin.site.register(Direction)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(CategoryNews)
admin.site.register(SubscribeNews)