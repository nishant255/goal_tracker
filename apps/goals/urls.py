from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^i2$', views.index2),
    url(r'^i3$', views.index3),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^new_goal$', views.new_goal),
    url(r'^create_goal$', views.create_goal),
    url(r'^goal/(?P<goal_id>\d+)$', views.goal),
    url(r'^update/(?P<goal_id>\d+)/(?P<minigoal_id>\d+)/(?P<update>\w+)$', views.update),
    url(r'^goal_log/$', views.goal_log),
]
