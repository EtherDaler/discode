from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myAuth.forms import UserCreationForm, UserChangeForm
from myAuth.models import User, UserManager
from .models import Category, Partner, Discounts, Images
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import gettext as _
from django.db.models import Q
from django.db.models import Count
import datetime
import random

def main(request):
	now = timezone.now()
	today = datetime.datetime.now()
	soon = []
	end_soon = None
	print(today.day)
	for i in Discounts.objects.filter(date_of_finish__gte = now).order_by('date_of_finish','date_of_create'):
		if i.date_of_finish.month == today.month and today.year == i.date_of_finish.year:
			if i.date_of_finish.day - today.day <= 7:
				soon.append(i)
	if len(soon) <= 4:
		this_week = soon[:]
	else:
		this_week = soon[:4]
	print(soon)
	print(this_week)
	if len(this_week) > 0:
		end_soon = this_week[0]

	categs = Category.objects.all().annotate(cnt=Count('discounts')).order_by('cnt')
	pop_categs = []
	it_cnt = 0
	for i in categs:
		it_cnt += 1
		if it_cnt == 3:
			break
		else:
			pop_categs.append(i)

	popular_discounts = []

	it_cnt = 0
	for discount in Discounts.objects.all().order_by('-watch','date_of_finish'):
		it_cnt += 1
		if it_cnt == 8:
			break
		else:
			popular_discounts.append(discount)

	new = []
	it_cnt = 0
	for discount in Discounts.objects.all().order_by('date_of_create'):
		it_cnt += 1
		if it_cnt == 8:
			break
		else:
			new.append(discount)

	context = {
		'categories': Category.objects.all(),
		'partners': Partner.objects.all(),
		'discounts': Discounts.objects.filter(date_of_finish__gte = now).order_by('active','date_of_finish','date_of_create'),
		'soon': this_week,
		'soon_count': len(this_week),
		'end_soon':end_soon,
		'popular_categories': pop_categs,
		'now': now,
		'popular_discounts': popular_discounts,
		'popular_discounts_length': len(popular_discounts),
		'new': new,
		'new_lenght': len(new),
	}
	return render(request, 'client/main.html', context)

def login_page(request):
	if request.method == 'POST':
		phone = request.POST.get('phone')
		password = request.POST.get('password')
		user = authenticate(request, phone=phone, password=password)
		if user is not None:
			login(request, user)
			return redirect('main')
		else:
			messages.info(request, 'Неверный номер телефона или пароль!')

	return render(request, 'auth/login.html')

def logout_page(request):
	logout(request)
	return redirect('main')

def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			print("work")
			user = form.save(commit = False)
			user.set_password(form.cleaned_data['password1'])
			form.save()
			user.save()
			login(request, user)
			return redirect('main_page')
	context = {
		'form':form,
	}
	return render(request, 'auth/register.html', context)

def profile(request):
	form = UserChangeForm(instance=request.user)
	if request.method == 'POST':
		form = UserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.info(request,"Профиль отредактирован")
			return redirect('profile')
	context = {
		'form': form,
		'categories': Category.objects.all(),
	}
	return render(request, 'auth/profile.html', context)

def about_us(request):
	return render(request, 'info/about_us.html')

def faq(request):
	return render(request, 'info/faq.html')

# политика конфиденциальности
def politic(request):
	return render(request, 'info/politic.html')

# Страница для клиентов о том, как это работает
def how_it_works(request):
	return render(request, 'info/how_it_works.html')

def contacts(request):
	return render(request, 'info/contacts.html')

# список акций
def list_discounts(request, *args, **kwargs):
    search_query = request.GET.get('search','')
    now = timezone.now()
    searchDiscounts = Discounts.objects.filter(date_of_finish__gte = now).order_by('active','date_of_finish','date_of_create')
    if search_query:
    	listDiscounts = Discounts.objects.filter(Q(name__icontains=search_query) )
    else:
    	messages.info(request, "Не найдено скидок по запросу")
    kwargs['list_discounts'] = Discounts.objects.filter(date_of_finish__gte = now).order_by('active','date_of_finish','date_of_create')
    discounts_list = listDiscounts
    paginator = Paginator(discounts_list, 10)# Пагинатор будет распределять наши поездки по страницам
    page = request.GET.get('page', 1)
    try:
        discounts_list = paginator.page(page)
    except PageNotAnInteger:
        discounts_list = paginator.page(1)
    except EmptyPage:
        discounts_list = paginator.page(paginator.num_pages)

    context={ # через этот словарь можно передавать текст в html
   'listDiscounts':discounts_list,
   'searchDiscounts':searchDiscounts,
   'categories': Category.objects.all(),
    }

    return render(request, "client/list.html", context)


	

# подробная инфа про акцию
def info(request, slug, pk):
	getDiscountInfo = Discounts.objects.get(id = pk, slug = slug)
	context = {
		'getDiscountInfo': getDiscountInfo,
		'categories': Category.objects.all(),
	}
	return render(request, "client/info.html", context)

# получение подписки
def subscribe(request):
	pass

# запрос на получение скидки
def get_discount(request, id):
	pass

# Страница инфы для партнеров
def for_partners(request):
	return render(request, 'info/for_partners.html')

# стать партнером
def became_partner(request):
	pass

# страница партнера
def partner_info(request):
	pass

# клиенты запросившие скидку
def clients(request):
	pass

# мои партнерские скидки (для партнеров)
def my_discounts(request):
	pass

# создать скидку
def create_discount(request):
	pass

# редактировать скидку
def edit_discount(request, id):
	pass

# удалить скидку
def delete_discount(request, id):
	pass



