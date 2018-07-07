from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from .models import Post



urlpatterns = [
    url(r'^$', views.stat, name='ss'),

    # url(r'auth/social', include('social_django.urls', namespace='social')),

    url(r'^register/$', views.login_user, name='register'),
    url(r'^detail/$', views.post_list, name='detail'),
    url(r'^detail/(?P<id>\d+)/$', views.post_detail, name='id_detail'),
    url(r'^create/$', views.create_post, name='postCreate'),
    url(r'^detail/(?P<id>\d+)/edit/$', views.post_update, name='postUpdate'),
    url(r'^detail/(?P<id>\d+)/delete/$', views.delete_post, name='postdelete'),
]