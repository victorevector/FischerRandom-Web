from django.conf.urls import patterns, url
from position_generator import views

urlpatterns = patterns('',
    url(r'^$',views.position_generator, name='position_generator'),
    )

