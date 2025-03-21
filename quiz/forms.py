from django import forms
from .models import Quiz, Question, Option

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description','image']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text', 'is_correct']
