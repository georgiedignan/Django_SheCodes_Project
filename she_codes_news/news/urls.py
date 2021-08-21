from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),   #/news/ (home page for the news)
    path('<int:pk>/', views.StoryView.as_view(), name='story'),  # e.g.  --> /news/3/
    #path to add a new story
    path('add-story/', views.AddStoryView.as_view(), name='newStory') #/news/add-story
]
