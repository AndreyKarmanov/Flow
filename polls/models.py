import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField("date published")

    def recent(self) -> bool:
        return self.pubDate >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self) -> str:
        return self.questionText
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choiceText
    
class Student(models.Model):
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    gender = models.CharField(max_length = 10, blank = True, null = True)
    age = models.DecimalField(max_digits = 7, decimal_places = 0, blank=True, null=True)
    major = models.CharField(max_length = 50, blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"