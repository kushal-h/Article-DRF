from django.urls import path, include
from .views import article_list, artilce_detail, ArticleARIViews, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    #path('article/', article_list),
    #path('detail/<int:pk>/', artilce_detail),
    path('articles/', ArticleARIViews.as_view()),
    path('details/<int:id>/', ArticleDetails.as_view()),
    path('generic/articles/<int:id>/', GenericAPIView.as_view()),

]