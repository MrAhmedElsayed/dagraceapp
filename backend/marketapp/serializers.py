from rest_framework import serializers

from .models import Product, Category, Slideshow


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SlideshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slideshow
        fields = '__all__'
