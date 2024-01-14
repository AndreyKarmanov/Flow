import django_tables2 as tables
from .models import Course


class CourseTable(tables.Table):

    code = tables.columns.Column(
        linkify=("polls:course", [tables.A("school.pk"), tables.A("pk")]),
        attrs={"th": {"class": "cursor-pointer"},
               "a" : {"class" : "underline text-blue cursor-pointer"}},
    )

    name = tables.columns.Column(
        verbose_name="Course",
        accessor=tables.A("name"),
        attrs={"th" : {"class" : " w-96"}, "td": {"class": "text-left"}},
    )

    class Meta:
        model = Course
        template_name = "partials/table.html"
        fields = ('code', 'name', 'rating', 'workload', 'utility', 'credits')


class CourseSearchTable(tables.Table):
    course = tables.columns.Column(
        linkify=("polls:course", [tables.A("school.pk"),
                 tables.A("department.pk"), tables.A("pk")]),
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
        attrs = {"style": "margin-bottom: 0;",
                 "class": "table table-hover rounded"}
        fields = ('course', 'department')
