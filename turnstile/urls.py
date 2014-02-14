from django.conf.urls import patterns, url

urlpatterns = patterns(
    'turnstile.views',
    url(r'^$', 'login', name='turnstile_login'),
    url(r'^add-account', 'add_account', name='turnstile_add_account'),
    url(r'^assignments', 'assignments', name='turnstile_assignments'),
)
