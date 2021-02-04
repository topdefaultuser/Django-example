# Generated by Django 3.1.6 on 2021-02-02 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название задачи')),
                ('text', models.TextField(verbose_name='Описание задачи')),
                ('data', models.DateTimeField(verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Коментарий')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.task')),
            ],
        ),
    ]