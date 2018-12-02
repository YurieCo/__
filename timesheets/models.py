from django.db import models

# Create your models here.

class Task(models.Model):
    task_description = models.CharField(max_length=200)
    task_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.task_name



class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=200)
    start_date = models.DateTimeField('start working on')
    end_date = models.DateTimeField('end working on')

    def __str__(self):
        return self.descriptions

