from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Category, Product, Slideshow
from .serializers import CategorySerializer, ProductSerializer, SlideshowSerializer


def home(request):
    return render(request, 'marketapp/home.html')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDetail(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class SlideshowViewSet(viewsets.ModelViewSet):
    queryset = Slideshow.objects.all()
    serializer_class = SlideshowSerializer
    permission_classes = [IsAuthenticated]
