
from django.contrib import admin
from database.models import *


class NoticeAdmin(admin.ModelAdmin):
    list_display=('notice','date')

class UserAdmin(admin.ModelAdmin):
    list_display=('username','user_type','password')

class StudentAdmin(admin.ModelAdmin):
    list_display=('userid','name')

class SubjectAdmin(admin.ModelAdmin):
    list_display=('userid','english','math')

class TeacherAdmin(admin.ModelAdmin):
    list_display=('userid','name')
    
admin.site.register(Notice,NoticeAdmin)
admin.site.register(CustomUser,UserAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Subject,SubjectAdmin)
# Register your models here.
