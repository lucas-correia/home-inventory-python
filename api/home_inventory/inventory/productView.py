from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from inventory.models import Product
from inventory.productSerializer import ProductSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_reference(request, reference):
    try:
        product = Product.objects.get(reference=reference)
    except Product.DoesNotExist:
        return JsonResponse({'message':'produto não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        product_serializer = ProductSerializer(product)
        return JsonResponse(product_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'produto excluido com sucesso!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def list_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.isValid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
