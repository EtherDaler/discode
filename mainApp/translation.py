from modeltranslation.translator import register, TranslationOptions
from .models import *

# тут регистрируем модели и указываем, какие поля нужно у них добавить с переводом

@register(Category)
class CategoryTranslateOptions(TranslationOptions):
	fields = ('name',)

@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('name', 'adress', 'contact_face')


@register(Felials)
class FelialsTranslationOptions(TranslationOptions):
    fields = ('adress',)


@register(Discounts)
class DiscountsTranslationOptions(TranslationOptions):
    fields = ('name', 'body')


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('product',)
