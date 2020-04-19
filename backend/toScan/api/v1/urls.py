from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ListToValidateViewSet

router = DefaultRouter()
router.register("listtovalidate", ListToValidateViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
