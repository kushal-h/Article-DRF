from django.urls import path
from .views import article_list, artilce_detail, ArticleARIViews, ArticleDetails

urlpatterns = [
   # path('article/', article_list),
    #path('detail/<int:pk>/', artilce_detail),
    path('articles/', ArticleARIViews.as_view()),
    path('details/<int:id>/', ArticleDetails.as_view())
]