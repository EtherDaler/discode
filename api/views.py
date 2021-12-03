from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from mainApp.models import *
from .serializers import *
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
import json
from django.utils import timezone
from django.db.models import Count
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers


class DiscountsViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.filter(date_of_finish__gte = now, active = True)

class ImagesViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()

def get_soon(request):
    now = timezone.now()
    soon = []
    it_cnt = 0
    for i in Discounts.objects.filter(date_of_finish__gte=now, active=True).order_by('date_of_finish',
                                                                                     'date_of_create'):
        it_cnt += 1
        if it_cnt == 8:
            break
        if i.date_of_finish.month == now.month and now.year == i.date_of_finish.year:
            if (i.date_of_finish.day - now.day <= 7) and (i.date_of_finish.day - now.day >= 0):
                soon.append(i)
            elif (i.date_of_finish.day - now.day <= 7) and (i.date_of_finish.day - now.day == 0) and (
                    i.date_of_finish.hour >= now.hour) and (i.date_of_finish.minute >= now.minute) and (
                    i.date_of_finish.second > now.second):
                soon.append(i)
    if len(soon) <= 4:
        this_week = soon[:]
    else:
        this_week = soon[:4]

    context = []
    for discount in this_week:
        context.append({
            'id': discount.id,
            'partner': discount.partner.id,
            'name': discount.name,
            "body": discount.body,
            "discount": discount.discount,
            "slug": discount.slug,
            "category": discount.category.id,
            "date_of_create": discount.date_of_create,
            "date_of_finish": discount.date_of_finish,
            "active": discount.active,
            "watch": discount.watch
        })

    return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder, ensure_ascii=False), content_type="application/json")


class SoonDiscountsViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    http_method_names = ['get', 'head']
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.filter(date_of_finish__gte = now, active = True)
    cont = []

    def retrieve(self, request, *args, **kwargs):
        soon = []
        it_cnt = 0
        for i in Discounts.objects.filter(date_of_finish__gte=self.now, active=True).order_by('date_of_finish',
                                                                                              'date_of_create'):
            it_cnt += 1
            if it_cnt == 8:
                break
            if i.date_of_finish.month == self.now.month and self.now.year == i.date_of_finish.year:
                if (i.date_of_finish.day - self.now.day <= 7) and (i.date_of_finish.day - self.now.day >= 0):
                    soon.append(i)
                elif (i.date_of_finish.day - self.now.day <= 7) and (i.date_of_finish.day - self.now.day == 0) and (
                        i.date_of_finish.hour >= self.now.hour) and (i.date_of_finish.minute >= self.now.minute) and (
                        i.date_of_finish.second > self.now.second):
                    soon.append(i)
        if len(soon) <= 4:
            this_week = soon[:]
        else:
            this_week = soon[:4]
        serializer = DiscountsSerializer(this_week, many=True)
        #return HttpResponse(json.dumps(self.get_soon), content_type="application/json")
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        soon = []
        it_cnt = 0
        for i in Discounts.objects.filter(date_of_finish__gte=self.now, active=True).order_by('date_of_finish',
                                                                                              'date_of_create'):
            it_cnt += 1
            if it_cnt == 8:
                break
            if i.date_of_finish.month == self.now.month and self.now.year == i.date_of_finish.year:
                if (i.date_of_finish.day - self.now.day <= 7) and (i.date_of_finish.day - self.now.day >= 0):
                    soon.append(i)
                elif (i.date_of_finish.day - self.now.day <= 7) and (i.date_of_finish.day - self.now.day == 0) and (
                        i.date_of_finish.hour >= self.now.hour) and (i.date_of_finish.minute >= self.now.minute) and (
                        i.date_of_finish.second > self.now.second):
                    soon.append(i)
        if len(soon) <= 4:
            this_week = soon[:]
        else:
            this_week = soon[:4]
        serializer = DiscountsSerializer(this_week, many=True)
        #return HttpResponse(json.dumps(self.get_soon), content_type="application/json")
        return Response(serializer.data)



class DiscountsPopular(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('-watch','date_of_finish')[:8]

class NewDiscounts(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('date_of_create')[:8]

class HotDiscounts(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.filter(date_of_finish__gte = now, active = True).order_by('-discount')[:8]

class CategoriesViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PopularCategoriesViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = CategorySerializer
    queryset = Category.objects.all().annotate(cnt=Count('discounts')).order_by('-cnt')[:3]

class PartnersViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()

class BlogsViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = BlogsSerializer
    queryset = Blog.objects.all()

class EventsViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = EventsSerializer
    queryset = Events.objects.all()

class CommentsViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

class NewsletterViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()

class ProductsViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

class AnotherPhonesViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = AnotherPhonesSerializer
    queryset = AnotherPhones.objects.all()

class FelialsViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    serializer_class = FelialsSerializer
    queryset = Felials.objects.all()





"""
APIView
class DiscountsView(APIView):
    def get(self, request):
        discounts = Discounts.objects.all()
        serializer = DiscountsSerializer(discounts, many=True)
        return Response({"discounts": serializer.data})

    def post(self, request):
        discount = request.data.get("discount")
        # Create an article from the above data
        serializer = DiscountsSerializer(data=discount)
        if serializer.is_valid(raise_exception=True):
            discount_saved = serializer.save()
        return Response({"success": "Discount '{}' created successfully".format(discount_saved.name)})

    def put(self, request, pk):
        saved_discount = get_object_or_404(Discounts.objects.all(), pk=pk)
        data = request.data.get('discount')
        serializer = DiscountsSerializer(instance=saved_discount, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            discount_saved = serializer.save()
        return Response({
            "success": "Discount '{}' updated successfully".format(discount_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        discount = get_object_or_404(Discounts.objects.all(), pk=pk)
        discount.delete()
        return Response({
            "message": "Discount with id `{}` has been deleted.".format(pk)
        }, status=204)
"""


"""Generic View"""
# Апедставление для API
# мы наследуем наш класс от CreateAPIView, ListAPIView, которые наследуются от ListModelMixin, CreateModelMixin,
# поэтому методы post и get на писать не нужно
# ListCreateAPIView наследуется от CreateAPIView, ListAPIView, что так же упрощает код

"""
class DiscountsView(ListCreateAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer
"""
"""
    
    def get(self, request, *args, **kwargs): # get запрос
        return self.list(request, *args, **kwargs)
"""
"""

    def partner_create(self, serializer): # Сохранение партнера у скидки
        partner = get_object_or_404(Partner, id=self.request.data.get('partner'))
        return serializer.save(partner=partner)

    def category_create(self, serializer): # Сохранение категории у скидки
        category = get_object_or_404(Category, id=self.request.data.get('category'))
        return serializer.save(category=category)

"""
"""
    def post(self, request, *args, **kwargs): # get запрос
        return self.create(request, *args, **kwargs)
"""
"""

    
# Класс для обновления скидок, выполняет put, patch запрос
# Также этот класс нужен для получения информации об отдельном объекте (get)
# А еще этот класс позволяет удалять отдельную статью (delete запрос)
class SingleDiscountView(RetrieveUpdateDestroyAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer
"""