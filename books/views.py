import random
import string
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from . import permissions as Book_permissions
from . import models as Book_models
from . import serializers as Book_serializers
from config.settings import SITE_URL
from .services import timelimit



# 사용자용 가계부 (가계부 주인 혹은 관리자만 접근 가능)

#가계부 생성,리스트 View
class SpendCreateListAPIView(generics.ListCreateAPIView):

    permission_classes = [Book_permissions.IsBookUserOrAdminUser]
    
    # 가계부 주인의 쿼리 가져오기
    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Book_models.Book.objects.filter(user=user_id).all()
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return Book_serializers.BookCreateSerializer
        else:
            return Book_serializers.BookSerializer

#가계부 조회,수정,삭제 view
class SpendRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [Book_permissions.IsBookUserOrAdminUser]
    
    def get_queryset(self):
        book_id = self.kwargs["pk"]
        user_id = self.kwargs["user_id"]
        book = Book_models.Book.objects.filter(user=user_id).all()
        return book.filter(pk=book_id)
    
    
    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return Book_serializers.BookPatchSerializer
        else:
            return Book_serializers.BookSerializer



# 관리자용 가계부(관리자만 접근 가능)

#admin용 가계부 생성 및 리스트 view
class AdminSpendCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book_models.Book.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return Book_serializers.BookCreateSerializer
        else:
            return Book_serializers.BookSerializer

#admin용 가계부 조회,수정,삭제 view
class AdminSpendRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Book_models.Book.objects.all()
    allowed_method = ("PATCH","DELETE","GET","OPTION")
    
    def get_queryset(self):
        book_id = self.kwargs["pk"]
        book = Book_models.Book.objects.all()
        return book.filter(pk=book_id)
    
    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return Book_serializers.BookPatchSerializer
        else:
            return Book_serializers.BookSerializer


# 원래 url -> 단축url로 변경
@api_view(["POST"])
def url_shortner(request):
    # 기본 DB에 저장되어 있는 경우
    try:
        url = Book_models.UrlShortner.objects.get(original_url=request.data["original_url"])
        serializer = Book_serializers.UrlSerializer(url)
        return Response(serializer.data)
    except: #변환해야하는 url의 경우
        serializer = Book_serializers.UrlSerializer(data=request.data)
        if serializer.is_valid():
            shorten_url = SITE_URL + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7)) #대소문자,숫자 조합된 단축url
            serializer.save(shorten_url=shorten_url)
            return Response(serializer.data)
        return Response({"message":"Not a Valid serializer"})

# 단축 url -> 원래url로 변경
@api_view(["GET"])
def redirect_url(request,new_url):
    url = SITE_URL + new_url
    obj = Book_models.UrlShortner.objects.get(shorten_url=url)
    if timelimit(obj.created_at):
        return HttpResponseRedirect(obj.original_url) # 단축url(shorten url)에 접근했을때 기본url(original url)로 redirect
    else:
        obj.delete() #시간초과된 단축url은 삭제
        return Response({"message":"시간이 초과 되었습니다. 새로운 url을 발급 받길 바랍니다."})
    
