# from questions.views import AboutView

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about$', views.about, name='about'),
    url(r'^get$', views.get_post, name='get'),
    url(r'^post$', views.get_post, name='post'),
    url(r'^$', views.index, name='home'),
    url(r'^hot$', views.hot, name='hot'),
    #    url(r'^question/(?P<question_id>[0-9]+)/', views.question, name='question'),
    #    url(r'^tag/(?P<request_tag>.+)/', views.tag, name="tag"),
    url(r'^question/(?P<question_id>\d+)/$', views.question, name='question'),
    url(r'^tag/(?P<tag>\w+)', views.tag, name="tag"),
    url(r'^login$', views.login, name="login"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^ask$', views.ask, name="ask"),
    url(r'^settings$', views.settings , name="settings"),
    #    url(r'^profile/edit/', profile_edit, name='profile_edit'),
    #    url(r'^profile/(?P<name>.*)/', profile, name='profile_page'),
    #    url(r'^answer/', question_answer, name='question_answer'),
]
