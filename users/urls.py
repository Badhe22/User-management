from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileView

router = DefaultRouter()
router.register(r'', UserViewSet)  # /api/users/

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]