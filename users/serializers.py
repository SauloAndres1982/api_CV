from rest_framework import serializers

from .models import User, Links, ResumeUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = "__all__"
        fields = ["id", "type_id", "identification", "photo", "country", "city", "address", "phone", "birthday", "occupation_job", "relocate", "is_recruiter", "groups", "user_permissions" ]

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"

class ResumeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUser
        fields = "__all__"