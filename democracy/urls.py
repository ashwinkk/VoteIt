from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'democracy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^threads/([0-9]+)/','forum.views.thread'),
    url(r'^threads/','forum.views.serve_forum_threads'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addquestion/$','adminacc.views.addQuestion'),
    url(r'^summary/$','adminacc.views.summary'),
    url(r'^chooseoption/$','users.views.chooseOption'),
    url(r'^announcements/$','forum.views.announcements'),
    url(r'^charts/$','adminacc.views.chartdata'),
    url(r'^adminannounce/$','adminacc.views.announce'),
]
