from django.contrib import admin

from turnstile.models import *

class AssignmentAdmin(admin.ModelAdmin):
    list_filter = ('course',)
admin.site.register(Assignment, AssignmentAdmin)

admin.site.register(Attachment)
admin.site.register(Course)
admin.site.register(Submission)
