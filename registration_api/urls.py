from django.conf.urls import url
from registration_api.views import register, activate


urlpatterns = [
    url(r'^register/$',
        register,
        name='registration_api_register'),
    url(r'^activate/(?P<activation_key>\w+)/$',
        activate,
        name='registration_activate'),
]
