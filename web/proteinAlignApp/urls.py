from django.urls import re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    re_path(r'^align/?$', views.AlignHome.as_view()),
    re_path(r'^aligned/?$', views.AlignHome.as_view(), name='postalignment'),
    # staticfiles_urlpatterns(),
]
