from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm
from mainApp.models import *

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	search_fields = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)

class FelialsInline(admin.StackedInline): # так мы можем обращаться к этой модели внутри другой модели сразу
	model = Felials

class AnotherPhonesFieldInline(admin.StackedInline):
	model = AnotherPhones

class PartnerAdmin(admin.ModelAdmin):
	list_display = ['owner', 'name', 'phone', 'adress', 'email', 'active', 'date_of_create']
	search_fields = ['name', 'phone']
	list_filter = ['active']
	inlines = [FelialsInline, AnotherPhonesFieldInline]

admin.site.register(Partner, PartnerAdmin)

class DiscountImagesInline(admin.StackedInline): # так мы можем обращаться к этой модели внутри другой модели сразу
	model = Images

class DiscountProductsFieldInline(admin.StackedInline):
	model = Products

class DiscountsAdmin(admin.ModelAdmin):
    list_display = ['partner', 'name', 'slug', 'discount', 'active', 'date_of_create', 'date_of_finish']
    list_filter = ['active', 'date_of_create', 'date_of_finish', 'partner']
    list_editable = ['discount', 'active'] # используется для задания полей, которые могут быть отредактированы на странице отображения списка сайта администрирования
    prepopulated_fields = {'slug': ('name', 'partner', 'discount')}
    search_fields = ['name', 'slug', 'id', 'partner']
    inlines = [DiscountImagesInline, DiscountProductsFieldInline]

admin.site.register(Discounts, DiscountsAdmin)

class RequestsAdmin(admin.ModelAdmin):
	search_fields = ['company_name', 'owner']
	list_filter = ['date_of_create']

