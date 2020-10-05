from django.urls import path
from .views import article_list, artilce_detail

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/', artilce_detail),
]