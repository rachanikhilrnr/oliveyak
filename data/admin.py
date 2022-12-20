from django.contrib import admin
from data.models import data
class admindata(admin.ModelAdmin):
    list_display=('fname','lname','rno','dept','problem','desc')
admin.site.register(data,admindata)
