from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^add_link/$', views.add_link, name='add_link'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]