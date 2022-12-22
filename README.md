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
permission으로 가계부 주인 혹은 관리자만 접근가능
### 2.Token을 이용하여 사용자 회원가입,로그인,로그아웃 구현
유저가 회원가입하면 토큰을 발급받아 쿠키에 저장\
username과 password를 입력받아 유저가 존재하면 로그인 => 회원가입처럼 토큰을 쿠키에 저장\
토큰이 저장되어 있는 쿠키를 삭제하면 로그아웃

### 3. 가계부 상세내역 url을 단축url로 변환
ex) http://127.0.0.1:8000/가계부/user_id:1/가계부_id:3/ => http://127.0.0.1:8000/adG75E 로 변환\
하지만 가계부 상세내역 url이 permission으로 인해 자기 주인 아니면 접근을 못하기에 단축url도 접근이 안됨 \
=> 이건 추후에 수정 할 예정(아마 permission을 수정하던지, 다른곳을 손 봐야 할 것 같다)





