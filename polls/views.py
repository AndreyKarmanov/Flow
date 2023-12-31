from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST, require_GET
from django.db.models import Q

from django_tables2 import SingleTableView, RequestConfig
from django_htmx.middleware import HtmxDetails

from .tables import SchoolTable, DepartmentTable, CourseTable, CourseSearchTable
from .models import School, Department, Course
from .forms import RegisterForm


class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@require_GET
def index(request):
    return render(request, "index.html")

class SchoolsView(SingleTableView):
    table_class = SchoolTable
    template_name = 'schools.html'
    paginate_by = 10

    def get(self, request: HtmxHttpRequest):
        schools = School.objects.all()
        schoolTable = self.table_class(schools)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(schoolTable)
        return render(request, self.template_name, {"table": schoolTable})


class SchoolView(SingleTableView):
    table_class = DepartmentTable
    template_name = 'school.html'
    paginate_by = 10

    def get(self, request: HtmxHttpRequest, school_id):
        school = get_object_or_404(School, pk=school_id)
        queryset = school.departments.all()
        departmentTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(departmentTable)

        if request.htmx:
            return render(request, 'base/table.html', {'table': departmentTable, 'school': school})

        return render(request, self.template_name, {'table': departmentTable, 'school': school})


class DepartmentView(SingleTableView):
    table_class = CourseTable
    template_name = 'department.html'
    paginate_by = 10

    def get(self, request: HtmxHttpRequest, school_id, department_id):
        school = get_object_or_404(School, pk=school_id)
        department = get_object_or_404(Department, pk=department_id)
        queryset = department.courses.all()
        courseTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(courseTable)

        if request.htmx:
            return render(request, 'base/table.html', {'table': courseTable, 'department': department, 'school': school})

        return render(request, self.template_name, {'table': courseTable, 'department': department, 'school': school})


class CourseView(SingleTableView):
    table_class = CourseTable
    template_name = 'course.html'
    paginate_by = 10

    def get(self, request: HtmxHttpRequest, school_id, department_id, course_id):
        school = get_object_or_404(School, pk=school_id)
        department = get_object_or_404(Department, pk=department_id)
        course = get_object_or_404(Course, pk=course_id)

        return render(request, self.template_name, {"course": course, "department": department, "school": school})


class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def get(self, request: HtmxHttpRequest):
        form = RegisterForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HtmxHttpRequest):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:index'))
        return render(request, self.template_name, {"form": form})


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request: HtmxHttpRequest):
        return render(request, self.template_name)


class SearchView(TemplateView):

    def post(self, request: HtmxHttpRequest):
        if not request.htmx: # only allow POST requests from htmx
            return HttpResponseNotAllowed(['POST'])

        searchValue = request.POST.get('search', '')
        if not searchValue:
            return render(request, 'base/empty.html')

        courses = Course.objects.filter(Q(name__icontains=searchValue) | Q(code__icontains=searchValue))[:5]
        table = CourseSearchTable(courses)

        return render(request, 'base/table.html', {'table': table, 'search_value': searchValue})
           

class InfiniteScroll(SingleTableView):
    table_class = CourseTable
    template_name = 'department2.html'
    paginate_by = 10

    def get(self, request: HtmxHttpRequest, school_id: int = 1):
        school = get_object_or_404(School, pk=school_id)
        queryset = school.courses.all()
        courseTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(courseTable)
        
        if request.htmx:
            print("htmx")
            # print out the html that will be returned for debugging
            print(render(request, 'base/partialTable.html', {'table': courseTable, 'school': school}).content)
            return render(request, 'base/partialTable.html', {'table': courseTable, 'school': school})
        
        return render(request, self.template_name, {'table': courseTable, 'school': school})
