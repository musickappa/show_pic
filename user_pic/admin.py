from django.contrib import admin
from .models import Piclist,Myprofile
# Register your models here.



class List_Picture(admin.ModelAdmin):
    list_display = ['user', 'place','season','image']
    # list_display = ['place','season','image']
class List_Profile(admin.ModelAdmin):
    list_display = ['full_name' ,'career', 'feature','location','profile_img']


admin.site.register(Piclist,List_Picture)

admin.site.register(Myprofile,List_Profile)