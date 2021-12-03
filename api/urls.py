from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('discounts', DiscountsViewSet)
router.register('popular_discounts', DiscountsPopular)
router.register('new_discounts', NewDiscounts)
router.register('hot_discounts', HotDiscounts)
router.register('categories', CategoriesViewSet)
router.register('popular_categories', PopularCategoriesViewSet)
router.register('partners', PartnersViewSet)
router.register('images', ImagesViewSet)
router.register('urgent', SoonDiscountsViewSet)
router.register('blogs', BlogsViewSet)
router.register('events', EventsViewSet)
router.register('comments', CommentsViewSet)
router.register('newsletter', NewsletterViewSet)
router.register('products', ProductsViewSet)
router.register('another_phones', AnotherPhonesViewSet)
router.register('felials', FelialsViewSet)



urlpatterns = router.urls