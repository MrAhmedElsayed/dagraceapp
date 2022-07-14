from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductList, ProductDetail, SlideshowViewSet, CategoryViewSet
from .views import home

router = DefaultRouter()
router.register('category', CategoryViewSet),
router.register('slideshow', SlideshowViewSet),

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('product/', ProductList.as_view(), name='productList'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='ProductDetail'),
]
