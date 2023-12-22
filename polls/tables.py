import django_tables2 as tables
from .models import Question, Choice


class QuestionTable(tables.Table):
    class Meta:
        model = Question
        fields = ("questionText", "pubDate")

class ChoiceTable(tables.Table):
    class Meta:
        model = Choice
        fields = ("choiceText", "votes")

class QuestionChoiceTable(tables.Table):
    class Meta:
        model = Question
        fields = ("questionText", "pubDate", "choice_set")