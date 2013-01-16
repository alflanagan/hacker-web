from django.contrib import admin
from members.models import MemberProfile, MemberInterests
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class MemberInterestsAdmin(admin.ModelAdmin):

    save_on_top = True
    list_display = ('name','notes')
    actions_selction_counter = True

def toggle_profile_staff_user(obj, action=True):
    a = User.objects.get(username=obj)
    a.is_staff = action
    a.save()

def activate_members(modeladmin, request, queryset):
    #this allows you to process a workflow from the django admin panel to "activate" a member. the initial is to make them a "staff" user. This can grow as needed.
    for obj in queryset:
        toggle_profile_staff_user(obj)
activate_members.short_description = "Activate selected users"

def deactivate_members(modeladmin, request, queryset):
    #this allows you to process a workflow from the django admin panel to "de-activate" a member. the initial is to make them a "staff" user. This can grow as needed.
    for obj in queryset:
        toggle_profile_staff_user(obj, action=False)
deactivate_members.short_description = "De-Activate selected users"

def add_to_trainer_group(obj):
    a = Group.objects.get(name='Trainers')
    a.user_set.add(obj.user)
    a.save()

def remove_trainer_group(obj):
   a = Group.objects.get(name='Trainers')
   a.user_set.remove(obj.user)
   a.save()

def make_trainer_member(modeladmin, request, queryset):
    #if they're not already, marks the user as a trainer (adds to the trainer group)
    for obj in queryset:
        add_to_trainer_group(obj)
make_trainer_member.short_description = "Add selected users to the Trainers group"

def remove_trainer_member(modeladmin, request, queryset):
    #removes someone from trainer group
    for obj in queryset:
        remove_trainer_group(obj)
remove_trainer_member.short_description = "Remove selected users from the Trainers group"

class MemberProfileAdmin(admin.ModelAdmin):

    save_on_top = True
    actions_selection_counter = True
    list_display = ('user','get_full_name', 'is_staff', 'display_email', 'hackerspace', 'is_trainer')
    actions = [activate_members, deactivate_members, make_trainer_member, remove_trainer_member]




admin.site.register(MemberProfile, MemberProfileAdmin)
admin.site.register(MemberInterests, MemberInterestsAdmin)
