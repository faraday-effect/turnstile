from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from unipath import Path

class Course(models.Model):
    number = models.CharField(max_length=20)
    title = models.CharField(max_length=80)

    def __unicode__(self):
        return "{0} - {1}".format(self.number, self.title)


def handout_path(assignment, filename):
    return "handouts/{0}/{1}/{2}".format(slugify(assignment.course.number),
                                         slugify(assignment.name),
                                         filename)

class Assignment(models.Model):
    name = models.CharField(max_length=80)
    course = models.ForeignKey(Course)
    due_date = models.DateField()
    handout = models.FileField(upload_to=handout_path)

    class Meta:
        ordering = ('-due_date',)

    def __unicode__(self):
        return self.name

    @classmethod
    def all_by_course(cls):
        """Return a list of assignments by course."""
        by_course_id = { }
        # { course_id: { course: <course>,
        #                assignments: [ <assignment>, <assignment>, ... ] },
        #   course_id: { ... } }
        for assignment in cls.objects.all():
            course = assignment.course
            if course.pk not in by_course_id:
                by_course_id[course.pk] = { 'course': course,
                                            'assignments': [ assignment ] }
            else:
                by_course_id[course.pk]['assignments'].append(assignment)

        by_course = [ ]
        # [ { course: <course>,
        #     assignments: [ <assignment>, <assignment>, ... ] }, ... ]
        sorted_courses = sorted([ elt['course'] for elt in by_course_id.values() ],
                                key=lambda course: course.number)
        for course in sorted_courses:
            sorted_assignments = sorted(by_course_id[course.id]['assignments'],
                                        key=lambda assignment: assignment.due_date,
                                        reverse=True)
            by_course.append({ 'course': course,
                               'assignments': sorted_assignments })
        return by_course


class Submission(models.Model):
    student = models.ForeignKey(User, related_name='submissions')
    assignment = models.ForeignKey(Assignment, related_name='submissions')
    created_at = models.DateTimeField(auto_now=True)
    graded = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('view_submissions', "Can view submissions" ),
        )

    def __unicode__(self):
        return "{0}'s {1}".format(self.student.get_full_name(), self.assignment)


def attachment_path(attachment, filename):
    submission = attachment.submission
    return "attachments/{0}/{1}/{2}/{3}".format(slugify(submission.assignment.course.number),
                                                slugify(submission.assignment.name),
                                                slugify(submission.student.get_full_name()),
                                                filename)

class Attachment(models.Model):
    submission = models.ForeignKey(Submission, related_name='attachments')
    uploaded_at = models.DateTimeField(auto_now=True)
    uploaded_file = models.FileField(upload_to=attachment_path)

    def __unicode__(self):
        return Path(self.uploaded_file.url).name
