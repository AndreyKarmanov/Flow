from django.contrib import admin

from polls.models import School, Department, Course

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Course)