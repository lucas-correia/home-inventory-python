from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from inventory.models import Shelf
from inventory.shelfSerializer import ShelfSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT', 'DELETE'])
def shelf_detail_id(request, id):
    try:
        shelf = Shelf.objects.get(id=id)
    except Shelf.DoesNotExist:
        return JsonResponse({'message':'local não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        shelf_serializer = ShelfSerializer(shelf)
        return JsonResponse(shelf_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        shelf_data = JSONParser().parse(request)
        shelf_serializer = ShelfSerializer(shelf, data=shelf_data)
        if shelf_serializer.is_valid():
            shelf_serializer.save()
            return JsonResponse(shelf_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(shelf_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        shelf.delete()
        return JsonResponse({'message': 'local excluido com sucesso!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def list_shelfs(request):
    if request.method == 'GET':
        shelfs = Shelf.objects.all()
        shelfs_serializer = ShelfSerializer(shelfs, many=True)
        return JsonResponse(shelfs_serializer.data, safe=False)

    elif request.method == 'POST':
        shelf_data = JSONParser().parse(request)
        shelf_serializer = ShelfSerializer(data=shelf_data)
        if shelf_serializer.isValid():
            shelf_serializer.save()
            return JsonResponse(shelf_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(shelf_serializer.errors, status=status.HTTP_400_BAD_REQUEST)