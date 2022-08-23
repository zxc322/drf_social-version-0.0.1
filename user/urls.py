from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.ListUsers.as_view()),
    path('create/', views.CreateUser.as_view()),
    path('add_inter/', views.CreateOwnInterest.as_view()),
    path('user/<int:pk>/', views.RetApiView.as_view()),
    path('user_upd/<int:pk>/', views.UpdDelApiView.as_view()),
    #path('<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'})),
]