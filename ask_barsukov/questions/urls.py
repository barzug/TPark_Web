#from questions.views import AboutView

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about$', views.about, name='about'),
    url(r'^get$', views.get_post, name='get'),
    url(r'^post$', views.get_post, name='post'),
]