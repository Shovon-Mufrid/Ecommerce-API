from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
# Create your views here.
from .models import Category, Brand, Product

from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryViewset(viewsets.ViewSet):
     queryset = Category.objects.all()

     @extend_schema(responses = CategorySerializer)
     def list(self, request):
          serializers = CategorySerializer(self.queryset, many=True)
          return Response(serializers.data)
   
     
class BrandViewset(viewsets.ViewSet):
     queryset = Brand.objects.all()

     @extend_schema(responses = BrandSerializer)
     def list(self, request):
          serializers = BrandSerializer(self.queryset, many=True)
          return Response(serializers.data)     
     

class ProductViewset(viewsets.ViewSet):
     queryset = Product.objects.all()

     @extend_schema(responses = ProductSerializer)
     def list(self, request):
          serializers = ProductSerializer(self.queryset, many=True)
          return Response(serializers.data)     