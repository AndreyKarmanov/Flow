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
        linkify=("polls:depatment", [tables.A("school.pk"), tables.A("pk")]),
        verbose_name="Department",
        accessor=tables.A("name"),
    )

    class Meta:
        model = Department
        fields = ('name', 'school')


class CourseTable(tables.Table):
    name = tables.columns.Column(
        linkify=("polls:course", [tables.A("school.pk"), tables.A("department.pk"), tables.A("pk")]),
        verbose_name="Course",
        accessor=tables.A("name"),
    )

    class Meta:
        model = Course
        template_name = "infinite/table.html"
        fields = ('code', 'name', 'department', 'credits')


class CourseSearchTable(tables.Table):
    course = tables.columns.Column(
        linkify=("polls:course", [tables.A("school.pk"), tables.A("department.pk"), tables.A("pk")]),
        verbose_name="Course",
        accessor=tables.A("name"),
        attrs={"a": {"href": lambda record: record.get_absolute_url()}},
        empty_values=(),
        orderable=False,
    )

    def render_course(self, value, record):
        return f"{record.code} — {record.name}"

    class Meta:
        model = Course
        show_header = False
        template_name = "infinite/table.html"
        attrs = {"style": "margin-bottom: 0;", "class": "table table-hover rounded"}
        fields = ('course', 'department')
