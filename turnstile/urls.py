from django.conf.urls import patterns, url

urlpatterns = patterns(
    'turnstile.views',
    url(r'^add-account/$', 'add_account', name='turnstile_add_account'),
    url(r'^assignments/$', 'assignments', name='turnstile_assignments'),
    url(r'^assignments/(?P<assignment_id>\d+)/$', 'submit', name='turnstile_submit'),
    url(r'^home/$', 'home', name='turnstile_home'),
    url(r'^login/$', 'login', name='turnstile_login'),
    url(r'^logout/$', 'logout', name='turnstile_logout'),
    url(r'^attachment/(?P<attachment_id>\d+)/delete$', 'delete_attachment', name='turnstile_attachment_delete'),

    url(r'^submissions/$', 'list_submissions', name='turnstile_list_submissions'),
    url(r'^grade/(?P<submission_id>\d+)/$', 'grade_submission', name='turnstile_grade_submission'),
)
