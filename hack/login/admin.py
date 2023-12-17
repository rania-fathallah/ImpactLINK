from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EmployeeAccount
from profileUser.models import Profile

admin.site.register(EmployeeAccount, UserAdmin)



