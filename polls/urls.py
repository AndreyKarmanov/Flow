from django.urls import path

from . import views

app_name = "polls" # why are the nameing conventions different here? kind of annoying
urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("question_list/", views.question_list, name="question_list"),
    path('get_student_list/', views.get_student_list, name='get_student_list'),
    path('add_student', views.add_student, name='add_student'),
    path('add_student_submit', views.submit_new_student, name='add_student_submit'),
    path('add_student_cancel', views.cancel_add_student, name='add_student_cancel'), 
    path('<int:student_pk>/delete_student', views.delete_student, name='delete_student'),
    path('<int:student_pk>/edit_student', views.edit_student, name='edit_student'),
    path('<int:student_pk>/edit_student_submit', views.edit_student_submit, name='edit_student_submit'),
]