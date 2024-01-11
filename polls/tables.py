import django_tables2 as tables
from .models import School, Department, Course


class SchoolTable(tables.Table):
    name = tables.columns.Column(
        linkify=("polls:courses", [tables.A("pk")]),
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

    courseCount = tables.columns.Column(
        accessor="courses.count",
        verbose_name="Course Count"
    )

    averageRating = tables.columns.Column(
        accessor="courses.aggregate(Avg('rating'))['rating__avg']",
        verbose_name="Average Rating"
    )

    class Meta:
        model = Department
        fields = ('name', 'courseCount', 'averageRating')


class CourseTable(tables.Table):
    name = tables.columns.Column(
        linkify=("polls:course", [tables.A("school.pk"), tables.A("department.pk"), tables.A("pk")]),
        verbose_name="Course",
        accessor=tables.A("name"),
        attrs={"th" : {"class": "w-8 cursor-pointer"}, "a": {"class": "text-sans text-ellipsis w-full h-full"}},
    )

    code = tables.columns.Column(
        attrs={"th" : {"class": "w-8 cursor-pointer"}, "td": {"class": "text-left"}},
    )

    credits = tables.columns.Column(
        attrs={"th" : {"class": "w-8 cursor-pointer"}},
    )

    class Meta:
        model = Course
        template_name = "partials/table.html"
        fields = ('code', 'name', 'credits')


class CourseSearchTable(tables.Table):
    course = tables.columns.Column(
        linkify=("polls:course", [tables.A("school.pk"), tables.A("department.pk"), tables.A("pk")]),
        verbose_name="Course",
        accessor=tables.A("name"),
        empty_values=(),
        orderable=False,
    )

    def render_course(self, value, record):
        return f"{record.code} — {record.name}"

    class Meta:
        model = Course
        show_header = False
        template_name = "partials/table.html"
        attrs = {"style": "margin-bottom: 0;", "class": "table table-hover rounded"}
        fields = ('course', 'department')
