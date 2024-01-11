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
    template_name = 'tableView.html'
    paginate_by = 20

    def get(self, request: HtmxHttpRequest, school_id: int = None):

        if request.htmx:
            return self.post(request, school_id)

        queryset = Course.objects.all()
        school = None

        if school_id is not None:
            school = get_object_or_404(School, pk=school_id)
            queryset = school.courses.all()
        
        courseTable = self.table_class(queryset)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(courseTable)


        
        if school is not None:
            return render(request, self.template_name, {'table': courseTable, 'school': school})
        
        return render(request, self.template_name, {'table': courseTable})
    
    def post(self, request: HtmxHttpRequest, school_id: int = None):
        if not request.htmx: # only allow POST requests from htmx
            return HttpResponseNotAllowed(['POST'])
        
        print(request.POST)
        
        # build the filter query
        filterQuery = Q()
        if request.POST.get('search', False):
            filterQuery = filterQuery & Q(name__icontains=request.POST.get('search'))
        if request.POST.get('minCredits', False):
            filterQuery = filterQuery & Q(credits__gte=request.POST.get('minCredits'))
        if request.POST.get('maxCredits', False):
            filterQuery = filterQuery & Q(credits__lte=request.POST.get('maxCredits'))
        if request.POST.get('minRating', False):
            filterQuery = filterQuery & Q(rating__gte=request.POST.get('minRating'))
        if request.POST.get('maxRating', False):
            filterQuery = filterQuery & Q(rating__lte=request.POST.get('maxRating'))
        if request.POST.get('minDifficulty', False):
            filterQuery = filterQuery & Q(difficulty__gte=request.POST.get('minDifficulty'))
        if request.POST.get('maxDifficulty', False):
            filterQuery = filterQuery & Q(difficulty__lte=request.POST.get('maxDifficulty'))
        if request.POST.get('minWorkload', False):
            filterQuery = filterQuery & Q(workload__gte=request.POST.get('minWorkload'))
        if request.POST.get('maxWorkload', False):
            filterQuery = filterQuery & Q(workload__lte=request.POST.get('maxWorkload'))

        
        if school_id is not None:
            school = get_object_or_404(School, pk=school_id)
            filterQuery = filterQuery & Q(school=school)

        courses = Course.objects.filter(filterQuery)
        table = CourseTable(courses)
        RequestConfig(request, paginate={'per_page': self.paginate_by}).configure(table)

        if request.GET.get('scroll', False):
            return render(request, 'partials/tableExtension.html', {'table': table, 'school': school})
        return render(request, 'partials/table.html', {'table': table, 'school': school})
    
class InfiniteDepartments(SingleTableView):
    table_class = DepartmentTable
    template_name = 'tableView.html'
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