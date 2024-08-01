from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from .serializer import UserSerializer
from products.models import Products
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import logging
import json
from django.contrib.auth import login
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


logger = logging.getLogger(__name__)
# Create your views here.
@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        # Parse form data
        form = UserSerializer(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({'message': 'User created successfully'}, status=201)
        else:
            logger.error(f"Form errors: {form.errors}")
            return Response({'error': 'User creation failed', 'details': form.errors}, status=400)
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse('User logged in successfully', status=200)
        else:
            return HttpResponse('User login failed', status=400)
        

@api_view(['GET'])
# @permission_classes([IsAuthenticated]) 
def userpurchased(request):
    if request.method == 'GET':
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('User not logged in', status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])   
def addproduct(request):
    if request.method == 'POST':
        user = request.user
        product = Products.objects.get(id=request.POST['product_id'])
        user.Product.add(product)
        return HttpResponse('Product added to cart', status=200)
    else:
        return HttpResponse('User not logged in', status=401)