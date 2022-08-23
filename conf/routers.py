from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('user/', include('user.urls')),
    path('posts/', include('posts.urls')),
    path('subs/', include('followers.urls')),
    path('comments/', include('comments.urls')),
    path('feed/', include('feed.urls')),
    path('like/', include('likes.urls')),
]

# swagger urls

schema_view = get_schema_view(
    openapi.Info(
        title="zxc social API",
        default_version='v1',
        description="docs by swagger (zxcSocial.322)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
