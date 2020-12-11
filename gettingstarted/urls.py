from django.urls import path, include

from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

import hello.views


urlpatterns = [
    path("", hello.views.index, name="index"),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'accounts/signup/', hello.views.signup, name='signup')
]
