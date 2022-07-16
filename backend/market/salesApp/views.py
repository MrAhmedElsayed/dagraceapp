from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# from market.salesApp.models import Category,  SlidesModel  #Product
# from market.salesApp.serializers import CategorySerializer,  SlideshowSerializer # ProductSerializer,


def sales_app(request):
    return render(request, "salesApp/salesApp.html")


# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticated]


# class ProductList(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class ProductDetail(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]


# class SlideshowViewSet(viewsets.ModelViewSet):
#     queryset = SlidesModel.objects.all()
#     serializer_class = SlideshowSerializer
#     permission_classes = [IsAuthenticated]
