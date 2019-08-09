
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    # call in the allauth urls here - test it out with the default
    # allauth urls here ie, signin , signup ie 127.0.0.1:8000/accounts/login
    re_path(r'^accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
]