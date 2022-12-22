from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from rest_framework import status
import jwt
from . import models as User_models
from . import serilalizers as User_serializers
from config.settings import SECRET_KEY

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = User_serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            # 쿠키에 access,refresh토큰을 저장 ("access":access_token,"refresh":refresh_token)
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Method마다 유저정보, 로그인, 로그아웃 나누기 (GET:유저정보,POST:로그인,DELETE:로그아웃)

class AuthUserAPIView(APIView):
    
    # user정보 가져오기
    def get(self,request):
        try:
            access = request.COOKIES["access"]
            payload = jwt.decode(access,SECRET_KEY,algorithms=['HS256'])
            pk = payload["user_id"]
            user = get_object_or_404(User_models.User,pk=pk)
            serializer = User_serializers.AuthUserSerializer(instance=user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except(jwt.exceptions.ExpiredSignatureError):  # 토큰 만료 시 토큰 갱신
            data = {'refresh': request.COOKIES.get('refresh', None)}
            serializer = TokenRefreshSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                access = serializer.data.get('access', None)
                refresh = serializer.data.get('refresh', None)
                payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(User_models.User, pk=pk)
                serializer = User_serializers.AuthUserSerializer(instance=user)
                res = Response(serializer.data, status=status.HTTP_200_OK)
                res.set_cookie('access', access)
                res.set_cookie('refresh', refresh)
                return res
            raise jwt.exceptions.InvalidTokenError

        except(jwt.exceptions.InvalidTokenError): # 사용 불가능한 토큰일 때
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # 유저 로그인
    
    def post(self, request):
    	# 유저 인증
        user = authenticate(
            username=request.data.get("username"), password=request.data.get("password")
        )
        if user is not None:  # 이미 회원가입 된 유저일 때
            serializer = User_serializers.AuthUserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            return Response({"message":"등록되지 않은 ID이거나 비밀번호가 일치하지 않습니다."},status=status.HTTP_400_BAD_REQUEST)
    
    #로그아웃, 쿠키에서 토큰 삭제
    def delete(self, request):
        response = Response({
            "message": "Logout success"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response

