import datetime

from django.forms import (ModelForm, TextInput, Textarea, DateField)
from .models import (Task, Comment)


class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'text']

		widgets = {
			'title': TextInput(attrs={
				'type': 'input',  
				'class': 'form-control',
				'id': 'exampleFormControlInput1',
				'placeholder': 'коротко о задаче',
			}),

			'text': Textarea(attrs={
				'class': 'form-control',
				'id': 'exampleFormControlTextarea1',
				'rows': '3',
				'placeholder': 'детальное описание задачи',
			}),
		}


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['text']

		widgets = {
			'text': Textarea(attrs={
				'class': 'form-control',
				'id': 'exampleFormControlTextarea1',
				'rows': '3',
				'placeholder': 'детальное описание задачи',
			}),
		}