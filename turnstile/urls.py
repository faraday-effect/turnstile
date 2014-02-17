from django.conf.urls import patterns, url

urlpatterns = patterns(
    'turnstile.views',

    url(r'^add-account/$', 'add_account', name='ts-add-account'),
    url(r'^login/$', 'login', name='ts-login'),
    url(r'^logout/$', 'logout', name='ts-logout'),

    url(r'^home/$', 'home', name='ts-home'),

    url(r'^assignments/$', 'list_assignments', name='ts-list-assignments'),
    url(r'^assignments/(?P<assignment_id>\d+)/$', 'submit_attachments', name='ts-submit-attachments'),
    url(r'^attachment/(?P<attachment_id>\d+)/delete$', 'delete_attachment', name='ts-delete-attachment'),

    url(r'^submissions/$', 'list_submissions', name='ts-list-submissions'),
    url(r'^grade/(?P<submission_id>\d+)/$', 'grade_submission', name='ts-grade-submission'),
)
