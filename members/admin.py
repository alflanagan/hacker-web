from django.contrib import admin
from members.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(UserProfile, UserProfileAdmin)
