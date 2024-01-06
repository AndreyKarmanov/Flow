from rest_framework import serializers
from .models import School, Course, Department, Review

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["name", "country", "website", "description"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name", "school", "lastUpdated"]

class CourseSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True) 
    class Meta:
        model = Course
        fields = ["code", "department_name", "name", "school", "department", "description", "credits", "url", "lastUpdated", "extra"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["course", "user", "rating", "difficulty", "useful", "comment", "lastUpdated", "anonymous"]

