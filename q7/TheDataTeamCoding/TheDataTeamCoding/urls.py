from django.conf.urls import include, url
from django.contrib import admin
from question1.views import index, process
urlpatterns = [
    # Examples:
    # url(r'^$', 'TheDataTeamCoding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^process$', process),
]
