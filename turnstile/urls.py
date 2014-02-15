from django.conf.urls import patterns, url

urlpatterns = patterns(
    'turnstile.views',
    url(r'^$', 'login', name='turnstile_login'),
    url(r'^add-account/$', 'add_account', name='turnstile_add_account'),
    url(r'^assignments/$', 'assignments', name='turnstile_assignments'),
    url(r'^assignments/(?P<assignment_id>\d+)/$', 'submit', name='turnstile_submit'),
    url(r'^submission/(?P<submission_id>\d+)/delete$', 'delete_submission',
        name='turnstile_submission_delete'),

    url(r'^submissions/$', 'list_submissions', name='turnstile_list_submissions'),
)
