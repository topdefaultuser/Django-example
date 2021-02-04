from django.db import models


class Task(models.Model):
	title = models.CharField('Название задачи', max_length=150)
	text = models.TextField('Описание задачи')
	completed = models.BooleanField(default=0)

	def __str__(self):
		return self.title


	def is_completed(self):
		return self.completed
 

	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'


class Comment(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	text = models.CharField('Комментарий', max_length=200)


	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

