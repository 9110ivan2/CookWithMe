from django.contrib import admin
from accounts.models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin): #check why is this needed. 
    list_display = ("user",)
    search_fields= ('id',)

admin.site.register(Profile, ProfileAdmin)