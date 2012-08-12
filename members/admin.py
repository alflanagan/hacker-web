from django.contrib import admin
from members.models import UserProfile, MemberLevel

class MemberLevelAdmin(admin.ModelAdmin):

    save_on_top = True

class UserProfileAdmin(admin.ModelAdmin):

    save_on_top = True
    readonly_fields = ('account_number','membership_change_date')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(MemberLevel, MemberLevelAdmin)
