from modeltranslation.translator import translator,TranslationOptions
from .models import *


class DirectionTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class CategoryNewsTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Direction, DirectionTranslationOptions) 
translator.register(News, NewsTranslationOptions) 
translator.register(CategoryNews, CategoryNewsTranslationOptions) 