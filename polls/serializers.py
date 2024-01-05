from rest_framework import serializers
from .models import School, Course, Department, Review

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["name", "country", "website", "description"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["code", "name", "school", "department", "description", "credits", "url", "lastUpdated", "extra"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name", "school", "lastUpdated"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["course", "user", "rating", "difficulty", "useful", "comment", "lastUpdated", "anonymous"]

