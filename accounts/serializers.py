from rest_framework import serializers 
from django.contrib.auth.models import User

from accounts.models import Profile

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta: 
        model = User 
        fields= "__all__"
        

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = "__all__"