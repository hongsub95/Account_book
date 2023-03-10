## Start Project
virtualenv : poetry\
Web Framework : Django, Django Rest Framework(DRF)\
DB : mysql\
Token : simple-jwt

## DB (mysql 5.7.40)
### DB 모델 : Book(가계부), User(유저), Url(단축url)
### DB 스키마
가계부(book) : title(제목),spend_cate(소비,지출),money(금액),spend_date(소비날짜),bio(세부사항),user(유저),created_at,updated_at\
\
단축url(url) : original_url(원래 url), shorten_url(단축 url), created_at(생성날짜)\
\
유저(user) : name(이름),gender(성별),birthday(생일),email(이메일),created_at,updated_at

## 구현(DRF)
### 1.가계부 생성,수정,조회,삭제 구현
permission으로 로그인한 유저 혹은 관리자만 접근가능
### 2.Token을 이용하여 사용자 회원가입,로그인,로그아웃 구현
유저가 회원가입하면 토큰을 발급받아 쿠키에 저장\
username과 password를 입력받아 유저가 존재하면 로그인 => 회원가입처럼 토큰을 쿠키에 저장\
토큰이 저장되어 있는 쿠키를 삭제하면 로그아웃

### 3. 가계부 상세내역 url을 단축url로 변환
ex) http://127.0.0.1:8000/가계부/user_id:1/가계부_id:3/ => http://127.0.0.1:8000/adG75E 로 변환\


## 코드 리뷰
### 가계부 Create, List view
    class SpendCreateListAPIView(generics.ListCreateAPIView): 

        permission_classes = [Book_permissions.IsBookUserOrAdminUser] 

        def get_queryset(self):
            user_id = self.kwargs["user_id"]
            return Book_models.Book.objects.filter(user=user_id).all()

        def get_serializer_class(self):
            if self.request.method == "POST":
                return Book_serializers.BookCreateSerializer
            else:
                return Book_serializers.BookSerializer
### 가계부 retrieve, update, delete view
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
### Permission
    class IsBookUserOrAdminUser(BasePermission):

        def has_permission(self, request, view):
            if request.user and request.user.is_staff:
                return bool(True)
            user_id = view.kwargs.get('user_id', None)
            return bool(request.user and user_id == request.user.pk)
### 원래url -> 단축url
     @api_view(["POST"])
     def url_shortner(request)
     try:
         url = Book_models.UrlShortner.objects.get(original_url=request.data["original_url"])
         serializer = Book_serializers.UrlSerializer(url)
         return Response(serializer.data)
     except: 
         serializer = Book_serializers.UrlSerializer(data=request.data)
         if serializer.is_valid():
             shorten_url = SITE_URL + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7)) #대소문자,숫자 조합된 단축url
             serializer.save(shorten_url=shorten_url)
             return Response(serializer.data)
         return Response({"message":"Not a Valid serializer"})
 ### 단축url -> 원래url
    def redirect_url(request,new_url):
        url = SITE_URL + new_url
        obj = Book_models.UrlShortner.objects.get(shorten_url=url)
        if timelimit(obj.created_at):
            return HttpResponseRedirect(obj.original_url) # 단축url(shorten url)에 접근했을때 기본url(original url)로 redirect
        else:
            obj.delete() #시간초과된 단축url은 삭제
            return Response({"message":"시간이 초과 되었습니다. 새로운 url을 발급 받길 바랍니다."})


