from . import models as Book_models
from users import models as User_models

def gen_book(apps,schema_editor):
    
    title = "컴퓨터"
    spend_cate = "Expenditure"
    money = 1000000
    spend_date = "2022-06-30"
    bio = "코딩 하기 위해 삼"
    user1 = User_models.User.objects.get(pk=2)
    book1_1 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user1)
    book1_1.save()
    
    title = "저녁식사"
    spend_cate = "Expenditure"
    money = 60000
    spend_date = "2022-07-15"
    bio = "친구와 외식"
    user1 = User_models.User.objects.get(pk=2)
    book1_2 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user1)
    book1_2.save()
    
    title = "커피"
    spend_cate = "Expenditure"
    money = 5000
    spend_date = "2022-07-16"
    bio = "아침 커피"
    user1 = User_models.User.objects.get(pk=2)
    book1_3 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user1)
    book1_3.save()
    
    title = "머리 염색"
    spend_cate = "Expenditure"
    money = 80000
    spend_date = "2022-05-12"
    bio = "분위기 전환 겸 염색 함"
    user2 = User_models.User.objects.get(pk=3)
    book2_1 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user2)
    book2_1.save()
    
    title = "옷"
    spend_cate = "Expenditure"
    money = 180000
    spend_date = "2022-10-19"
    bio = "코트하나 삼"
    user2 = User_models.User.objects.get(pk=3)
    book2_2 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user2)
    book2_2.save()
    
    title = "애플패드"
    spend_cate = "Expenditure"
    money = 700000
    spend_date = "2022-05-12"
    bio = "카페에서 공부하기 위해 삼"
    user2 = User_models.User.objects.get(pk=3)
    book2_3 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user2)
    book2_3.save()
    
    
    title = "핸드폰"
    spend_cate = "Expenditure"
    money = 1300000
    spend_date = "2022-09-10"
    bio = "고장나서 바꿈"
    user3 = User_models.User.objects.get(pk=4)
    book3_1 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user3)
    book3_1.save()
    
    title = "게임"
    spend_cate = "Expenditure"
    money = 1000000
    spend_date = "2022-10-20"
    bio = "게임 현질"
    user3 = User_models.User.objects.get(pk=4)
    book3_2 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user3)
    book3_2.save()
    
    title = "핸드폰"
    spend_cate = "Expenditure"
    money = 1300000
    spend_date = "2022-09-10"
    bio = "고장나서 바꿈"
    user3 = User_models.User.objects.get(pk=4)
    book3_3= Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user3)
    book3_3.save()
    
    title = "책상 중고"
    spend_cate = "Income"
    money = 50000
    spend_date = "2022-03-20"
    bio = "다른걸로 사기 위해 중고로 팜"
    user4 = User_models.User.objects.get(pk=5)
    book4_1 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user4)
    book4_1.save()
    
    title = "지갑"
    spend_cate = "Expenditure"
    money = 350000
    spend_date = "2022-02-20"
    bio = "***지갑 삼"
    user4 = User_models.User.objects.get(pk=5)
    book4_2 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user4)
    book4_2.save()
    
    title = "술"
    spend_cate = "Income"
    money = 50000
    spend_date = "2022-08-10"
    bio = "친구와 술마신 후 더치페이"
    user4 = User_models.User.objects.get(pk=5)
    book4_3 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user4)
    book4_3.save()
    
    
    title = "신발"
    spend_cate = "Expenditure"
    money = 160000
    spend_date = "2022-08-16"
    bio = "바꿀때가 되어서 바꿈"
    user5 = User_models.User.objects.get(pk=6)
    book5_1 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user5)
    book5_1.save()
    
    title = "병원"
    spend_cate = "Expenditure"
    money = 13000
    spend_date = "2022-09-09"
    bio = "감기걸려서 병원비"
    user5 = User_models.User.objects.get(pk=6)
    book5_2 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user5)
    book5_2.save()
    
    title = "헬스장"
    spend_cate = "Expenditure"
    money = 320000
    spend_date = "2022-05-16"
    bio = "6개월치 헬스비"
    user5 = User_models.User.objects.get(pk=6)
    book5_3 = Book_models.Book(title=title,spend_cate=spend_cate,money=money,spend_date=spend_date,bio=bio,user=user5)
    book5_3.save()
    
    