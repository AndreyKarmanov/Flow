from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    country = models.CharField(max_length=60, blank=False, null=False)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/schools/{self.pk}/"

class Department(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.school.name})"
    
    def get_absolute_url(self):
        return f"/schools/{self.school.pk}/departments/{self.pk}/"

class Course(models.Model):
    code = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='courses')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    description = models.CharField(max_length=500, blank=True, null=True)
    credits = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    lastUpdated = models.DateTimeField(auto_now=True)
    extra = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.code} {self.name}"
    
    def get_absolute_url(self):
        return f"/schools/{self.school.pk}/departments/{self.department.pk}/courses/{self.pk}/"
    
class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    
    rating = models.IntegerField(blank=False, null=False, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    difficulty = models.IntegerField(blank=False, null=False, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    useful = models.IntegerField(blank=False, null=False, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    comment = models.CharField(max_length=500, blank=True, null=True)
    lastUpdated = models.DateTimeField(auto_now=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.code} {self.course.name} - {self.user.username}"
    
    def get_absolute_url(self):
        return f"/schools/{self.course.school.pk}/departments/{self.course.department.pk}/courses/{self.course.pk}/reviews/{self.pk}/"