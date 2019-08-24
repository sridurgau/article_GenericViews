from django.urls import path

from .views import SingleArticleView, ArticleView


app_name = "article"


urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
    path('articles/<int:pk>', SingleArticleView.as_view()),
]