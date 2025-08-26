from django.urls import path
from .views import TweetListCreateView

app_name = 'tweet'

urlpatterns = [
    path('', TweetListCreateView.as_view(), name='list'),
]

