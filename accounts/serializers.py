from rest_framework import serializers 
from django.contrib.auth.models import User

from accounts.models import Profile

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta: 
        model = User 
        fields= "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data.get("email", ""),
            password = validated_data["password"],
            first_name = validated_data.get("first_name", ""),
            last_name = validated_data.get("last_name", ""),
        )   
        return user
        

class ProfileSerializer(serializers.ModelSerializer):
    pass