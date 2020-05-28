from django.contrib import admin
from django.urls import path, include
from quizz_app.views import index
from quizz_app.api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
from django.conf import settings
from django.conf.urls import url
from django.views.generic.base import TemplateView

routes = getattr(settings, 'REACT_ROUTES', [])

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/', include('quizz_app.urls')),
    path('', index, name="index"),
    url(r'^(%s)?$' % '|'.join(routes), TemplateView.as_view(template_name='index.html')),

]

