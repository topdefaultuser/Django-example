# Generated by Django 3.1.6 on 2021-02-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='data',
            new_name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=200, verbose_name='Комментарий'),
        ),
    ]