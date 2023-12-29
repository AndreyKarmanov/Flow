from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views.generic import TemplateView
from django.forms import ModelForm, modelform_factory
from .tables import SchoolTable, DepartmentTable, CourseTable
from .models import School, Department, Course
from django.views.decorators.http import require_POST, require_GET
from django_tables2 import SingleTableView
from django_tables2 import SingleTableView, RequestConfig
from django.contrib.auth.models import User

from .forms import RegisterForm

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
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(schoolTable)
        return render(request, self.template_name, {"schoolTable": schoolTable})


class SchoolView(SingleTableView):
    table_class = DepartmentTable
    template_name = 'school.html'
    paginate_by = 10

    def get(self, request, school_id):
        school = get_object_or_404(School, pk=school_id)
        queryset = school.departments.all()
        departmentTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(departmentTable)
        return render(request, self.template_name, {"departmentTable": departmentTable, "school": school})


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

        return render(request, self.template_name, {"courseTable": courseTable, "department": department, "school": school})


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
