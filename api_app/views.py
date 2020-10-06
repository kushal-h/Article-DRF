from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import  Articleserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

#class for Artilce if we write views the help of class
class ArticleARIViews(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = Articleserializers(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Articleserializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ArticleDetails(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id =id)

        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = Articleserializers(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = Articleserializers(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def article_list(request):
# viewing articles
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = Articleserializers(articles, many=True)
        return Response(serializer.data)

#posting the article
    elif request.method == 'POST':
        serializer = Articleserializers(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# Viewing article details
@api_view(['GET', 'PUT', 'DELETE'])
def artilce_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Articleserializers(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Articleserializers(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        article.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)
