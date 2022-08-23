from django.urls import path
from . import views


urlpatterns = [
    path('users_post/<int:pk>/', views.LikedPostUsersListAPIView.as_view()),
    path('users_comment/<int:pk>/', views.LikedCommentUsersListAPIView.as_view()),
    path('<slug:slug>/<int:pk>/', views.AddRemoveLikeView.as_view()),

    # path('user/<int:pk>/', views.UsersFollowersView.as_view()),
    # path('user/follows/<int:pk>/', views.UserFollowsView.as_view()),
    # path('i_follow/', views.UsersIFollowView.as_view()),
    # path('', views.MyFollowersView.as_view())
]