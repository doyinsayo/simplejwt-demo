from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserViewSet

# Registering Rest-API routes for Accounts
router = DefaultRouter()
router.register(r'user', views.UserViewSet, 'user')

urlpatterns = [
    path('', include(router.urls), name='accounts_api'),
]