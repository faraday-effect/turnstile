from django.contrib import admin

from turnstile.models import *

admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Submission)
