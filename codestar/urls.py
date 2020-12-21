from django.conf.urls import url
from codestar import views

urlpatterns = [
	url(r'^$',views.greetings),
	url(r'^testing$',views.testing),
    url(r'^home/run$',views.runcode),
]
