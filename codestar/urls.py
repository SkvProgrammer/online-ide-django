from django.urls import path, re_path
from codestar import views

urlpatterns = [
    path('', views.greetings, name='greetings'),  # Simple path for the root URL
    path('testing', views.testing, name='testing'),  # Simple path for 'testing'
    re_path(r'^home/run$', views.runcode, name='run_code'),  # Regex-based pattern for 'home/run'
]
