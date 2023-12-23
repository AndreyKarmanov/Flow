import django_tables2 as tables
from django.urls import reverse
from .models import School, Department, Course


class SchoolTable(tables.Table):
    name = tables.columns.Column(
        linkify=True,
        verbose_name="School",
        accessor=tables.A("name"),
        
    )
    
    class Meta:
        model = School
        fields = ('name', 'country', 'website', 'description')


class DepartmentTable(tables.Table):
    class Meta:
        model = Department
        fields = ('name', 'school', 'description')


class CourseTable(tables.Table):
    class Meta:
        model = Course
        fields = ('code', 'name', 'school', 'department', 'description', 'credits', 'url')
