from django.contrib import admin

from turnstile.models import *

class AssignmentAdmin(admin.ModelAdmin):
    list_filter = ('course',)
admin.site.register(Assignment, AssignmentAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('assignment',)
admin.site.register(Comment, CommentAdmin)


admin.site.register(Attachment)
admin.site.register(Course)
admin.site.register(Feedback)
admin.site.register(Submission)


