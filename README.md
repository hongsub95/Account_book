## Start Project
virtualenv : poetry\
Web Framework : Django, Django Rest Framework(DRF)\
DB : mysql\
Token : simple-jwt

### DB (mysql 5.7.40)
#### DB 모델 : Book(가계부), User(유저), Url(단축url)
#### DB 스키마
가계부(book) : title(제목),spend_cate(소비,지출),money(금액),spend_date(소비날짜),bio(세부사항),user(유저),created_at,updated_at\
\
단축url(url) : original_url(원래 url), shorten_url(단축 url), created_at(생성날짜)\
\
유저(user) : name(이름),gender(성별),birthday(생일),email(이메일),created_at,updated_at




