from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
<<<<<<< HEAD
admin.site.register(CustomUser,UserAdmin)
=======
# admin.site.unregister(User)
admin.site.register(CustomUser,UserAdmin)
>>>>>>> origin/master
