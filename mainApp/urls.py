from django.urls import path, include
from .views import *

urlpatterns = [
	path('', main, name = 'main'),
	path('login/', login_page, name = 'login'),
	path('logout/', logout_page, name = 'logout'),
	path('profile/', profile, name = 'profile'),
	path('list/', list_discounts, name = 'list_discounts'),
	path('info/<slug:partner>/<int:pk>-<slug:slug>', info, name = 'info'),
	path('add_comment/', add_comment, name='add_comment'),
]