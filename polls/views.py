from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views.generic import TemplateView
from django.forms import ModelForm, modelform_factory
from .tables import SchoolTable, DepartmentTable, CourseTable
from .models import School, Department, Course, Student
from django.views.decorators.http import require_POST, require_GET
from django_tables2 import SingleTableView
from django_tables2 import SingleTableView, RequestConfig
from django.contrib.auth import authenticate, login


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



class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        form = modelform_factory(Student, fields=('email',))
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):
        form = modelform_factory(Student, fields=('email',))(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = authenticate(request, username=email)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error('email', 'Email does not exist.')
        return render(request, self.template_name, {"form": form})

# Create your views here.
# @require_GET
# def index(request):
#     latestQuestions = Question.objects.order_by("-pubDate")[:5]
#     context = {
#         "latestQuestions": latestQuestions,
#     }
#     return render(request, "index.html", context)

# @require_GET
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "detail.html", {"question": question})

# @require_GET
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "results.html", {"question": question})


# @require_POST
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1 # this avoids a race condition by using the database to increment the votes field (this will be translated to SQL)
#         # use refresh_from_db() to reload the object from the database, if you need to access the new value of votes.
#         # if you do multiple save() the votes will be incremented multiple times, as F("votes") + 1 is not evaluated until the object is saved.
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# @require_GET
# def question_list(request):
#     questions = Question.objects.all()
#     return render(request, "question_list.html", {"questions": questions})


# class HomePageView(TemplateView):
#     template_name = 'base.html'

# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         exclude = []

# def get_student_list(request):
#     context = {}
#     context['students'] = Student.objects.all()
#     return render(request, 'student_list.html', context)

# def add_student(request):
#     context = {'form': StudentForm()}
#     return render(request, 'partial/student/add_student.html', context)

# def submit_new_student(request):
#     context = {}
#     form = StudentForm(request.POST)
#     context['form'] = form
#     if form.is_valid():
#         context['student'] = form.save()
#     else:
#         return render(request, 'partial/student/add_student.html', context)
#     return render(request, 'partial/student/student_row.html', context)

# def cancel_add_student(request):
#     return HttpResponse()

# def delete_student(request, student_pk):
#     student = Student.objects.get(pk=student_pk)
#     student.delete()
#     return HttpResponse()


# def edit_student(request, student_pk):
#     student = Student.objects.get(pk=student_pk)
#     context = {}
#     context['student'] = student
#     context['form'] = StudentForm(initial={
#         'first_name':student.first_name,
#         'last_name': student.last_name,
#         'gender': student.gender,
#         'age': student.age,
#         'major': student.major
#     })
#     return render(request, 'edit_student.html', context)

# def edit_student_submit(request, student_pk):
#     context = {}
#     student = Student.objects.get(pk=student_pk)
#     context['student'] = student
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#         else:
#             return render(request, 'edit_student.html', context)
#     return render(request, 'student_row.html', context)
