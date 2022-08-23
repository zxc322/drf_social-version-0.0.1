from django.urls import path
from . import views


urlpatterns = [
    path('comment/', views.CommentsView.as_view({'post': 'create'})),
    path('comment/<int:pk>/', views.CommentsView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('comment_child/<int:pk>/', views.Comment2Comment.as_view()),
    ]
