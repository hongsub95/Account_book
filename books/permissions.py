from rest_framework.permissions import BasePermission
from . import models as Book_models
from users import models as User_models

#가계부 주인 계정 혹은 관리자만 접근 가능

class IsLoginUserOrAdminUser(BasePermission):

    def has_permission(self, request, view):
        if request.user or request.user.is_staff:
            return bool(True)
        


        