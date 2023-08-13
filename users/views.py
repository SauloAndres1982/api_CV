from rest_framework import viewsets

from .models import User, Links, ResumeUser
from .serializers import UserSerializer, LinksSerializer, ResumeUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class ResumeUserViewSet(viewsets.ModelViewSet):
    queryset = ResumeUser.objects.all()
    serializer_class = ResumeUserSerializer