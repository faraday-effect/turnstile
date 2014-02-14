from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=80)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

class Course(models.Model):
    name = models.CharField(max_length=80)

class Assignment(models.Model):
    name = models.CharField(max_length=80)
    due_date = models.DateField()
    handout = models.FileField(upload_to="handouts")

    def __unicode__(self):
        return self.name
