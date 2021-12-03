from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myAuth.forms import UserCreationForm, UserChangeForm
from myAuth.models import User, UserManager
from .models import Category, Partner, Discounts, Comments
from .forms import CommentsForm
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import gettext as _
from django.db.models import Q
from django.db.models import Count
import datetime
from django.http import HttpResponse
import random
from django.db.models import F
import json


# Вывод данных, для фильтрации предложений
class Filter:
	def get_partners(self):
		return Partner.objects.all()
	def get_categories(self):
		return Category.objects.all()

#NEW

def main(request):
	now = timezone.now()
	today = datetime.datetime.now()
	search_query = request.GET.get('search', '')
	if search_query:
		return redirect('/list/?search='+str(search_query))
	#Выводим предложения, на которые скоро заканчивается срок
	print(now)
	print(today)
	soon = []
	end_soon = None
	it_cnt = 0
	for i in Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('date_of_finish','date_of_create'):
		it_cnt += 1
		if it_cnt == 8:
			break
		if i.date_of_finish.month == today.month and today.year == i.date_of_finish.year:
			if (i.date_of_finish.day - today.day <= 7) and (i.date_of_finish.day - today.day >= 0):
				soon.append(i)
			elif (i.date_of_finish.day - today.day <= 7) and (i.date_of_finish.day - today.day == 0) and (i.date_of_finish.hour >= today.hour) and (i.date_of_finish.minute >= today.minute) and (i.date_of_finish.second > today.second): 
				soon.append(i)
	if len(soon) <= 4:
		this_week = soon[:]
	else:
		this_week = soon[:4]

	if len(this_week) > 0:
		end_soon = this_week[0]

	# Вывод популярных категорий
	categs = Category.objects.all().annotate(cnt=Count('discounts')).order_by('-cnt')
	pop_categs = []
	it_cnt = 0
	for i in categs:
		it_cnt += 1
		if it_cnt == 4:
			break
		else:
			pop_categs.append(i)

	popular_discounts = []

	# Популярные предложения
	it_cnt = 0
	for discount in Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('-watch','date_of_finish'):
		it_cnt += 1
		if it_cnt == 9:
			break
		else:
			popular_discounts.append(discount)

	# Новые предложения
	new = []
	it_cnt = 0
	for discount in Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('date_of_create'):
		it_cnt += 1
		if it_cnt == 9:
			break
		else:
			new.append(discount)

	# Самые горячие предложения
	such_discounts = []
	it_cnt = 0
	for discount in Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('-discount'):
		it_cnt += 1
		if it_cnt == 13:
			break
		else:
			such_discounts.append(discount)

	# Вывод списка категорий сбоку от карусели, чтобы они выводились красиво
	first_ct = []
	second_ct = []
	it_cnt = 0
	for category in Category.objects.all():
		if it_cnt >= 6:
			second_ct.append(category)
		else:
			first_ct.append(category)

		it_cnt += 1



	context = {
		'categories': Category.objects.all(),
		'soon': this_week,
		'soon_count': len(this_week),
		'end_soon':end_soon,
		'popular_categories': pop_categs,
		'now': now,
		'popular_discounts': popular_discounts,
		'popular_discounts_length': len(popular_discounts),
		'new': new,
		'new_lenght': len(new),
		'such_discounts': such_discounts,
		'such_discounts_length': len(such_discounts),
		'first_ct': first_ct,
		'second_ct': second_ct,
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
    now = timezone.now()
    today = datetime.datetime.now()
    search_query = request.GET.get('search','')
    category = request.GET.get('category', '')
    partner = request.GET.get('partner', '')
    now = timezone.now()
    searchDiscounts = Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('date_of_finish','date_of_create')
    if search_query:
    	listDiscounts = Discounts.objects.filter(Q(name__icontains=search_query)&Q(active=True)).order_by('date_of_finish','date_of_create')
    else:
    	listDiscounts = Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('date_of_finish','date_of_create')
    if listDiscounts.count() == 0:
        messages.info(request, "Не найдено скидок по запросу")

    if category or partner:
        listDiscounts = Discounts.objects.filter(Q(active=True) & Q(date_of_finish__gte=now) & Q(Q(category__in=category) | Q(partner__in=partner))).order_by(
			'date_of_finish', 'date_of_create')

    kwargs['discounts_list'] = Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('date_of_finish','date_of_create')
    discounts_list = listDiscounts
    paginator = Paginator(discounts_list, 10)# Пагинатор будет распределять наши поездки по страницам
    page = request.GET.get('page', 1)
    try:
        discounts_list = paginator.page(page)
    except PageNotAnInteger:
        discounts_list = paginator.page(1)
    except EmptyPage:
        discounts_list = paginator.page(paginator.num_pages)

    context = { # через этот словарь можно передавать текст в html
        'now': now,
        'listDiscounts': discounts_list,
		'listDiscounts_length': len(discounts_list),
        'searchDiscounts':searchDiscounts,
        'categories': Category.objects.all(),
		'filter': Filter,
    }

    return render(request, "client/list.html", context)


	

# подробная инфа про акцию
def info(request, partner, pk, slug):
	now = timezone.now()
	today = datetime.datetime.now()
	search_query = request.GET.get('search', '')
	rating_status = True
	if search_query:
		return redirect('/list/?search=' + str(search_query))

	getDiscountInfo = Discounts.objects.get(id=pk, slug=slug)

	sum = 0
	ct = 0

	for star in Comments.objects.filter(discount=getDiscountInfo):
		if int(star.rating) != 0:
			sum += int(star.rating)
			ct += 1
	try:
		rating = round(sum/ct,0)
	except:
		rating = 0

	try:
		user_comments = getDiscountInfo.comments.filter(user=request.user)
	except:
		user_comments = None
	if user_comments == None:
		pass
	else:
		for comment in user_comments:
			if comment.rating_used == True:
				rating_status = False

	can_show = True

	if getDiscountInfo.date_of_finish <= today:
		can_show = False

	getDiscountInfo.watch_up()
	getDiscountInfo.save()
	context = {
		'getDiscountInfo': getDiscountInfo,
		'categories': Category.objects.all(),
		'form': CommentsForm(),
		'rating_status': rating_status,
		'commetaries': Comments.objects.filter(discount=getDiscountInfo, active=True),
		'rating': rating,
		'can_show': can_show,
	}
	return render(request, "client/info.html", context)

# Добавление комментария(отзыва)

def add_comment(request):
	today = datetime.datetime.now()
	form = CommentsForm()
	if request.method == 'POST':
		form = CommentsForm(request.POST)
		if form.is_valid():
			response = {}
			disc = Discounts.objects.get(id=int(request.POST.get('discount')))
			Comments.objects.create(
				user=request.user,
				discount=disc,
				rating=request.POST.get('star_rating'),
				text=request.POST.get('text'),
				rating_used=True,
				date=today
			)
			response['result'] = 'Ваш комментарий успешно отправлен, модераторы проверят его в течение 24 часов.'

			return HttpResponse(
				json.dumps(response),
				content_type="application/json"
			)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

"""

def add_comment(request):
	today = datetime.datetime.now()
	if request.method == 'POST':
		user = request.user
		response_data = {}
		discount = request.POST.get('c_discount')
		rating = request.POST.get('c_star')
		comment = request.POST.get('c_text')
		Comments.objects.create(
			user=user,
			discount=discount,
			rating=rating,
			text=comment,
			rating_used=True,
			date=today
		)
		response_data['result'] = 'Success!!.'
		return HttpResponse(
			json.dumps({'result': 'Success', 'data': [discount,rating,comment]}),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)
"""

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



