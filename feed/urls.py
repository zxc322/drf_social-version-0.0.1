from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedAPIView.as_view())
    ]