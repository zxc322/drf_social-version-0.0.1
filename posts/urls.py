from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.PostListAPIView.as_view()),
    path('post/', views.PostView.as_view({'post': 'create'})),
    path('post/<int:pk>/', views.PostView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    #path('<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'})),
]