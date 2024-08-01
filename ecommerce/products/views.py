from django.shortcuts import render
from .models import Products
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework import generics
from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)



# Create your views here.

class GetLatestProducts(APIView):
    def get(self, request, format=None):
        products=Products.objects.all()[0:4]
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data)
    

# class ProductDetail(APIView):
#     def get(self,category_slug , product_slug , request, format=None):
#         try:
#             # product=Products.objects.filter(category__slug=category_slug).get(slug=product_slug)
#             product=Products.objects.get(slug=product_slug)
#         except Products.DoesNotExist as e:
#             return Response({'error': str(e)}, status=404)
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)

class ProductDetail(APIView):
    def get(self, request, product_slug, format=None):
        try:
            product = Products.objects.get(slug=product_slug)
        except Products.DoesNotExist as e:
            return Response({'error': str(e)}, status=404)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    


# to search the products
@api_view(['POST'])
def search(request):
    # get the query and seach on that query accordingly
    query = request.query_params.get('query','') # we needs to write the queryparam here as we are seing the query from the url
    if query:
        products = Products.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) #here the Q is used to search on the query like django rpovides it tfor the advance query search
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No query provided'})


class CreateProduct(APIView):
    parser_classes = [MultiPartParser, FormParser]
    http_method_names = ['post' , 'delete' , 'patch']
    # permission_classes = [IsAuthenticated]
    # permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        logger.info(request.data)
        data = {
            'category': request.data.get('category'),
            'name': request.data.get('name'),
            'slug': request.data.get('slug'),
            'description': request.data.get('description'),
            'price': request.data.get('price'),
            'image': request.FILES.get('image'),
            'thumbnail': request.FILES.get('thumbnail')
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk, format=None):
        try:
            product = Products.objects.get(pk=pk)
            product.delete()
        except Products.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        return Response(status=204 , data={'message': 'Product deleted successfully'})

    def patch(self, request, pk, format=None):
        try:
            product = Products.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Products.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)