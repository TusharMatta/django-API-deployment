from django.contrib import admin
from userapi.models import Custom_User, UserActivity

# Register your models here.


admin.site.register(Custom_User)
admin.site.register(UserActivity)
