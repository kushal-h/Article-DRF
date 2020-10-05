from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import  Articleserializers

# Create your views here.

def article_list(request):

    if request.methods == 'GET':
        articles = Article.objects.all()
        serializer = Articleserializers(articles, many=True)
        return JsonResponse(serilaizer.data, safe= False)

    elif request.methods == 'POST':
        data = JSONParser().parse(request)
        serializer = Articleserializers(data= data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)