from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Clothe
from .serializers import ClotheSerializer

@api_view(['POST', 'GET'])
def get_post_clothes(request):
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'clad_type': request.data.get('clad_type'),
            'color': request.data.get('color')
        }
        serializer = ClotheSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        clothes = Clothe.objects.all()
        serializer = ClotheSerializer(clothes, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def get_delete_update_clothes(request, pk):
    try:
        clothe = Clothe.objects.get(pk=pk)
    except Clothe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == 'GET':
        serializer = ClotheSerializer(clothe)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClotheSerializer(clothe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        clothe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)