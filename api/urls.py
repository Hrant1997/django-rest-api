from django.urls import include, path
from rest_framework import routers

from . import views

api_router = routers.DefaultRouter()

api_router.register(r'users', views.UserViewSet)


api_routes = [
    path('profiles/', views.ProfileViewSet.as_view()),
    path('profiles/<profile:profile>', views.ProfileDetailApiView.as_view())
]


for route in api_routes:
    api_router.urls.append(route)
    
urlpatterns = [
    path('api/v1/', include(api_router.urls)),
]
