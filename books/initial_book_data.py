from . import models as Book_models
from users import models as User_models

def gen_book(apps,schema_editor):
    
    title = "컴퓨터"
    spend_cate = "Expenditure"
    money = 1000000
    spend_date = "2022-06-30"
    bio = "코딩 하기 위해 삼"
    user1 = User_models.User.objects.get(pk=2)
    book1 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user1)
    book1.save()
    
    title = "머리 염색"
    spend_cate = "Expenditure"
    money = 1000000
    spend_date = "2022-05-12"
    bio = "분위기 전환 겸 염색 함"
    user2 = User_models.User.objects.get(pk=3)
    book2 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user2)
    book2.save()
    
    
    title = "핸드폰"
    spend_cate = "Expenditure"
    money = 1300000
    spend_date = "2022-09-10"
    bio = "고장나서 바꿈"
    user3 = User_models.User.objects.get(pk=4)
    book3 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user3)
    book3.save()
    
    
    title = "책상 중고"
    spend_cate = "income"
    money = 50000
    spend_date = "2022-03-20"
    bio = "다른걸로 사기 위해 중고로 팜"
    user4 = User_models.User.objects.get(pk=5)
    book4 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user4)
    book4.save()
    
    
    title = "신발"
    spend_cate = "Expenditure"
    money = 160000
    spend_date = "2022-08-16"
    bio = "바꿀때가 되어서 바꿈"
    user5 = User_models.User.objects.get(pk=6)
    book5 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user5)
    book5.save()
    
    