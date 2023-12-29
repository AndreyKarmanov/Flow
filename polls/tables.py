import django_tables2 as tables
from .models import School, Department, Course


class SchoolTable(tables.Table):
    name = tables.columns.Column(
        linkify=("polls:school", [tables.A("pk")]),
        verbose_name="School",
        accessor=tables.A("name"),
    )

    class Meta:
        model = School
        fields = ('name', 'country', 'website', 'description')


class DepartmentTable(tables.Table):
    name = tables.columns.Column(
        linkify=("polls:department", [tables.A("school.pk"), tables.A("pk")]),
        verbose_name="Department",
        accessor=tables.A("name"),
    )

    class Meta:
        model = Department
        fields = ('name', 'school', 'description')


class CourseTable(tables.Table):
    name = tables.columns.Column(
        linkify=("polls:course", [tables.A("school.pk"), tables.A("department.pk"), tables.A("pk")]),
        verbose_name="Course",
        accessor=tables.A("name"),
    )
    class Meta:
        model = Course
        fields = ('code', 'name', 'department', 'credits')
