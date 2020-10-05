from django.urls import path
from .views import article_list
urlpatterns = [
    path('admin/', article_list()),
]