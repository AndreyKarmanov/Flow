from django.urls import path

from . import views

app_name = "polls" # why are the nameing conventions different here? kind of annoying
urlpatterns = [
    path("", views.index, name="index"),
    path("schools/", views.SchoolsView.as_view(), name="schools"),
    path("schools/<int:school_id>/departments/", views.SchoolView.as_view(), name="school"),
    path("schools/<int:school_id>/departments/<int:department_id>/courses/", views.DepartmentView.as_view(), name="department"),
    path("schools/<int:school_id>/departments/<int:department_id>/courses/<int:course_id>/", views.CourseView.as_view(), name="course"),
]