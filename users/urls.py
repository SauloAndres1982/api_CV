from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet, LinksViewSet, ResumeUserViewSet

router = routers.DefaultRouter()

router.register(r'usuarios', UserViewSet, basename="usuarios")
router.register(r'links', LinksViewSet, basename="links")
router.register(r'resumen', ResumeUserViewSet, basename="resumen")


urlpatterns = [
    path("", include(router.urls)),
]
