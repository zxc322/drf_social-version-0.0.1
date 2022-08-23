from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.AddRemoveFollowerView.as_view()),
    path('user/<int:pk>/', views.UsersFollowersView.as_view()),
    path('user/follows/<int:pk>/', views.UserFollowsView.as_view()),
    path('i_follow/', views.UsersIFollowView.as_view()),
    path('', views.MyFollowersView.as_view())
]