from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import ApplicationViewSet, UserViewSet

router = DefaultRouter()
router.register('applications', ApplicationViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]