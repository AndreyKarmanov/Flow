from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST, require_GET
from django.db.models import Q

from django_tables2 import SingleTableView, RequestConfig
from django_htmx.middleware import HtmxDetails

from .tables import SchoolTable, DepartmentTable, CourseTable, CourseSearchTable
from .models import School, Department, Course
from .forms import RegisterForm

import uuid

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

@require_GET
def index(request):
    return render(request, "index.html")

class SchoolsView(SingleTableView):
    table_class = SchoolTable
    template_name = 'schools.html'
    paginate_by = 10

    def get(self, request):
        schools = School.objects.all()
        schoolTable = self.table_class(schools)
        RequestConfig(request, paginate={
                      'per_page': self.paginate_by}).configure(schoolTable)
        return render(request, self.template_name, {"table": schoolTable})


class SchoolView(SingleTableView):
    table_class = DepartmentTable
    template_name = 'school.html'
    paginate_by = 5

    def get(self, request, school_id):
        school = get_object_or_404(School, pk=school_id)
        queryset = school.departments.all()
        departmentTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(
            departmentTable)
        return render(request, self.template_name, {"table": departmentTable, "school": school, "unique_id": uuid.uuid4()})


class DepartmentView(SingleTableView):
    table_class = CourseTable
    template_name = 'department.html'
    paginate_by = 10

    def get(self, request, school_id, department_id):
        school = get_object_or_404(School, pk=school_id)
        department = get_object_or_404(Department, pk=department_id)
        queryset = department.courses.all()
        courseTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(courseTable)
        uid = str(uuid.uuid4())
        print(uid[:5])
        if request.htmx:
            return render(request, 'base/table.html', {'table': courseTable, 'department': department, 'school': school, 'unique_id': uid})
        
        return render(request, self.template_name, {"table": courseTable, "department": department, "school": school, "unique_id": uid})


class CourseView(SingleTableView):
    table_class = CourseTable
    template_name = 'course.html'
    paginate_by = 10

    def get(self, request, school_id, department_id, course_id):
        school = get_object_or_404(School, pk=school_id)
        department = get_object_or_404(Department, pk=department_id)
        course = get_object_or_404(Course, pk=course_id)

        return render(request, self.template_name, {"course": course, "department": department, "school": school})


class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:index'))
        return render(request, self.template_name, {"form": form})

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request):
        return render(request, self.template_name)
    
class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request):
        if request.htmx:
            return HttpResponse("Hello from htmx!")
        
        return render(request, self.template_name)
    
    def post(self, request):
        if request.htmx:
            search_value = request.POST.get('search', '')
            if not search_value:
                return render(request, 'partials/empty.html', {'table': None, 'search_value': search_value})
            
            courses = Course.objects.filter(Q(name__icontains=search_value) | Q(code__icontains=search_value))[:5]
            table = CourseSearchTable(courses)

            return render(request, 'partials/table.html', {'table': table, 'search_value': search_value})
        
        return HttpResponse("Hello from non-htmx!")