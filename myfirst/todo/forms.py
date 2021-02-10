from django.forms import ModelForm, TextInput, PasswordInput, Textarea, EmailInput
from django.forms import CharField, EmailField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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
				'rows': '5',
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
				'rows': '5',
				'placeholder': 'детальное описание задачи',
			}),
		}


class UserLoginForm(AuthenticationForm):
	username = CharField(label='Имя пользователя',
					widget=TextInput(attrs={'class': 'form-control'}))

	password = CharField(label='Пароль',
					widget=PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
	username = CharField(label='Имя пользователя',
						widget=TextInput(attrs={
							'class': 'form-control',
							'placeholder': 'Имя пользователя',
							'required': '',
						}))

	password1 = CharField(label='Пароль',
						widget=PasswordInput(attrs={
							'class': 'form-control',
							'placeholder': 'Пароль',
							'required': '',
						}))

	password2 = CharField(label='Повторите пароль',
						widget=PasswordInput(attrs={
							'class': 'form-control',
							'placeholder': 'Повторите пароль',
							'required': '',
						}))

	email = EmailField(label='Укажите e-mail',
						widget=EmailInput(attrs={
							'class': 'form-control',
							'placeholder': 'e-mail',
						}))


	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


