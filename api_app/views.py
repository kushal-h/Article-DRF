from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import  Articleserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

from pusher_push_notifications import PushNotifications
# Create your views here.

#view sets
'''
# Generic Viewsets
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,  mixins.DestroyModelMixin):
    serializer_class = Articleserializers
    queryset = Article.objects.all()
'''
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = Articleserializers
    queryset = Article.objects.all()



#views by generics and mixins
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = Articleserializers
    queryset = Article.objects.all()

    lookup_field = 'id'
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:

            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id= None):
        return self.update(request, id)

    def delete(self, grequest, id):
        return self.destroy(request=id)








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

'''
#notification

def push_notify(psst):
    beams_client = PushNotifications(
        instance_id='YOUR_INSTANCE_ID_HERE',
        secret_key='YOUR_SECRET_KEY_HERE',
    )
'''