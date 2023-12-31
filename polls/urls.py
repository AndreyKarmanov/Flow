from django.contrib import admin, auth
from django.urls import path, include

from . import views

app_name = "polls" # why are the nameing conventions different here? kind of annoying
urlpatterns = [
    path("", views.index, name="index"),
    path("schools/", views.SchoolsView.as_view(), name="schools"),
    path("schools/<int:school_id>/departments/", views.SchoolView.as_view(), name="school"),
    path("schools/<int:school_id>/departments/<int:department_id>/courses/", views.DepartmentView.as_view(), name="department"),
    path("schools/<int:school_id>/departments/<int:department_id>/courses/<int:course_id>/", views.CourseView.as_view(), name="course"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("infinitescroll/", views.InfiniteScroll.as_view(), name="infinitescroll"),
]