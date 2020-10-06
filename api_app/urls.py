from django.urls import path
from .views import article_list, artilce_detail, ArticleARIViews

urlpatterns = [
   # path('article/', article_list),
    path('detail/<int:pk>/', artilce_detail),
    path('articles/', ArticleARIViews.as_view())
]