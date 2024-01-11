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
from django.db.models import Avg, Sum



class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


class SchoolsView(SingleTableView):
    template_name = 'schools.html'
    def get(self, request: HtmxHttpRequest):
        queryset = School.objects.all()
        return render(request, self.template_name, {'schools' : queryset})

class CoursesTable(SingleTableView):
    table_class = CourseTable
    template_name = 'partials/table.html'
    paginate_by = 20

    def get(self, request: HtmxHttpRequest, school_id: int = None, department_id: int = None):

        if not request.htmx:
            return HttpResponseNotAllowed(['GET'])

        queryset = Course.objects.all()
        school = None
        department = None
        
        if department_id is not None:
            department = get_object_or_404(Department, pk=department_id)
            school = department.school
            queryset = department.courses.all()
        elif school_id is not None:
            school = get_object_or_404(School, pk=school_id)
            queryset = school.courses.all()

        courseTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(courseTable)
       
        return render(request, self.template_name, {'table': courseTable, 'school': school, 'department': department})
    
class InfiniteDepartments(SingleTableView):
    table_class = DepartmentTable
    template_name = 'department.html'
    paginate_by = 10

    def get(self, request: HtmxHttpRequest, school_id: int = None):
        if school_id is not None:
            school = get_object_or_404(School, pk=school_id)
            queryset = school.departments.all()
        else:
            queryset = Department.all()

        courseTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(courseTable)
        
        if not request.htmx:
            return render(request, self.template_name, {'table': courseTable, 'school': school})
        
        if request.GET.get('scroll', False):
            return render(request, 'partials/tableExtension.html', {'table': courseTable, 'school': school})
        
        if request.GET.get('sort', False):
            return render(request, 'partials/table.html', {'table': courseTable, 'school': school})
        
        return render(request, 'base/empty.html')




class SchoolView(SingleTableView):
    table_class = DepartmentTable
    template_name = 'temp.html'
    paginate_by = 10

    def get(self, request: HtmxHttpRequest, school_id: int):
        school = get_object_or_404(School, pk=school_id)
        queryset = school.departments.all()
        departmentTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(departmentTable)

        return render(request, self.template_name, {'table': departmentTable, 'school': school})


class CourseView(SingleTableView):
    table_class = CourseTable
    template_name = 'course.html'
    paginate_by = 10

    def get(self, request: HtmxHttpRequest, school_id: int, department_id: int, course_id: int):
        course = get_object_or_404(Course, pk=course_id)
        school = course.school
        department = course.department

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

        return render(request, 'partials/searchTable.html', {'table': table, 'search_value': searchValue})
    
class TempView(TemplateView):
    template_name = 'temp.html'

    def get(self, request: HtmxHttpRequest):
        return render(request, self.template_name)