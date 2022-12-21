from rest_framework.permissions import BasePermission

from . import models as Book_models
from users import models as User_models

#가계부 주인 계정 혹은 관리자만 접근 가능

class IsBookUserOrAdminUser(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return bool(True)
        user_id = view.kwargs.get('user_id', None)
        book = Book_models.Book.objects.filter(user=user_id).all()[0]
        return bool(request.user and book.user == request.user)