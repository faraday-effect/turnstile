from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from unipath import Path

class Course(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


def handout_path(instance, filename):
    return "handouts/{0}/{1}/{2}".format(slugify(instance.course.name),
                                         slugify(instance.name),
                                         filename)

class Assignment(models.Model):
    name = models.CharField(max_length=80)
    course = models.ForeignKey(Course)
    due_date = models.DateField()
    handout = models.FileField(upload_to=handout_path)

    def __unicode__(self):
        return self.name


def submission_path(instance, filename):
    return "submissions/{0}/{1}/{2}/{3}".format(slugify(instance.assignment.course.name),
                                                slugify(instance.assignment.name),
                                                slugify(instance.student.get_full_name()),
                                                filename)

class Submission(models.Model):
    student = models.ForeignKey(User, related_name='submissions')
    assignment = models.ForeignKey(Assignment, related_name='submissions')
    submitted_at = models.DateTimeField(auto_now=True)
    submitted_file = models.FileField(upload_to=submission_path)

    class Meta:
        permissions = (
            ('view_submissions', "Can view submissions" ),
        )

    def __unicode__(self):
        return Path(self.submitted_file.url).name
