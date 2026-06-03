from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['user']
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password= validated_data['password']
        )
        
        return user

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self):
        refresh_token = self.validated_data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()
        