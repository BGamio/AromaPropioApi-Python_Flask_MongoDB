from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Api.models import Post, Resennia, LibroDeReclamaciones
from Api.serializers import PostSerializaer, ResenniaSerializer, LibroDeReclamacionesSerializer


# Create your views here.

def home(request):
    return HttpResponse('Bienvenido a la API de Aroma Propio')

@csrf_exempt
def post_endpoint(request, id=0):
    if request.method == 'GET':
        post = Post.objects.all()
        post_serializer = PostSerializaer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializaer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=201)
        return JsonResponse(post_serializer.errors, status=400)

    elif request.method == 'PUT':
        post_data = JSONParser().parse(request)
        post = Post.objects.get(id=post_data['id'])
        post_serializer = PostSerializaer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=201)
        return JsonResponse(post_serializer.errors, status=400)

    elif request.method == 'DELETE':
        post = Post.objects.get(id=id)
        post.delete()
        return JsonResponse('Deleted Successfully', status=204)


@csrf_exempt
def resennia_endpoint(request, id=0):
    if request.method == 'GET':
        resennia = Resennia.objects.all()
        resennia_serializer = ResenniaSerializer(resennia, many=True)
        return JsonResponse(resennia_serializer.data, safe=False)

    elif request.method == 'POST':
        resennia_data = JSONParser().parse(request)
        resennia_serializer = ResenniaSerializer(data=resennia_data)
        if resennia_serializer.is_valid():
            resennia_serializer.save()
            return JsonResponse(resennia_serializer.data, status=201)
        return JsonResponse(resennia_serializer.errors, status=400)

    elif request.method == 'PUT':
        resennia_data = JSONParser().parse(request)
        resennia = Resennia.objects.get(id=resennia_data['id'])
        resennia_serializer = ResenniaSerializer(resennia, data=resennia_data)
        if resennia_serializer.is_valid():
            resennia_serializer.save()
            return JsonResponse(resennia_serializer.data, status=201)
        return JsonResponse(resennia_serializer.errors, status=400)

    elif request.method == 'DELETE':
        resennia = Resennia.objects.get(id=id)
        resennia.delete()
        return JsonResponse('Deleted Successfully', status=204)


@csrf_exempt
def libro_de_reclamaciones_endpoint(request, id=0):
    if request.method == 'GET':
        libro_de_reclamaciones = LibroDeReclamaciones.objects.all()
        libro_de_reclamaciones_serializer = LibroDeReclamacionesSerializer(libro_de_reclamaciones, many=True)
        return JsonResponse(libro_de_reclamaciones_serializer.data, safe=False)

    elif request.method == 'POST':
        libro_de_reclamaciones_data = JSONParser().parse(request)
        libro_de_reclamaciones_serializer = LibroDeReclamacionesSerializer(data=libro_de_reclamaciones_data)
        if libro_de_reclamaciones_serializer.is_valid():
            libro_de_reclamaciones_serializer.save()
            return JsonResponse(libro_de_reclamaciones_serializer.data, status=201)
        return JsonResponse(libro_de_reclamaciones_serializer.errors, status=400)

    elif request.method == 'PUT':
        libro_de_reclamaciones_data = JSONParser().parse(request)
        libro_de_reclamaciones = LibroDeReclamaciones.objects.get(id=libro_de_reclamaciones_data['id'])
        libro_de_reclamaciones_serializer = LibroDeReclamacionesSerializer(libro_de_reclamaciones, data=libro_de_reclamaciones_data)
        if libro_de_reclamaciones_serializer.is_valid():
            libro_de_reclamaciones_serializer.save()
            return JsonResponse(libro_de_reclamaciones_serializer.data, status=201)
        return JsonResponse(libro_de_reclamaciones_serializer.errors, status=400)

    elif request.method == 'DELETE':
        libro_de_reclamaciones = LibroDeReclamaciones.objects.get(id=id)
        libro_de_reclamaciones.delete()
        return JsonResponse('Deleted Successfully', status=204)
