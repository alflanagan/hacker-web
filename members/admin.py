from django.contrib import admin
from members.models import MemberProfile, MemberInterests

class MemberInterestsAdmin(admin.ModelAdmin):

    save_on_top = True

class MemberProfileAdmin(admin.ModelAdmin):

    save_on_top = True

admin.site.register(MemberProfile, MemberProfileAdmin)
admin.site.register(MemberInterests, MemberInterestsAdmin)
