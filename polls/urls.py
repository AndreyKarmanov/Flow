from django.contrib import admin, auth
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "polls" # why are the nameing conventions different here? kind of annoying
urlpatterns = [
    path("", views.SchoolsView.as_view(), name="index"),
    path("schools/", views.SchoolsView.as_view(), name="schools"),
    
    path("schools/<int:school_id>/courses", views.CoursesTable.as_view(), name="courses"), 
    path("schools/<int:school_id>/departments", views.InfiniteDepartments.as_view(), name="departments"),

    path("schools/<int:school_id>/departments/<int:department_id>/", views.CoursesTable.as_view(), name="department"),
    path("schools/<int:school_id>/departments/<int:department_id>/courses/<int:course_id>/", views.CourseView.as_view(), name="course"),
    path("accounts/register/", views.RegisterView.as_view(), name="register"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("search/", views.SearchView.as_view(), name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)