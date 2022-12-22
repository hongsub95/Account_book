from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import models as User_models

#토큰 페이로드에 유저 정보 담기

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['gender'] = user.gender
        token['name'] = user.name
        token['email'] = user.email
        token['is_staff'] = user.is_staff

        return token
    
class ApiRefreshRefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    pass

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_models.User
        fields = ('username','name','gender','email','password')

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        gender = validated_data.get('gender')
        name = validated_data.get('name')
        user = User_models.User(
            username=username,
            email=email,
            gender=gender,
            name=name
        )
        user.set_password(password)
        user.save()
        return user

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_models.User
        fields = ("pk","username","name","email","gender","is_staff")