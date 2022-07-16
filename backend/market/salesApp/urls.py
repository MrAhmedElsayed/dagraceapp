from django.urls import path
from rest_framework.routers import DefaultRouter

# from market.salesApp.views import (sales_app, SlideshowViewSet, CategoryViewSet)
from market.salesApp.views import sales_app

# app_name = "salesApp"

# router = DefaultRouter()
# router.register('category', CategoryViewSet),
# router.register('slideshow', SlideshowViewSet),

urlpatterns = [
    path("test/", view=sales_app, name="test-view"),
]
