from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # url(r'^$', views.Paipan.as_view(), name='index'),
    # url(r'^$', views.Jiegua.as_view(), name='index'),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^paipan/$', views.Paipan.as_view(), name='paipan'),
    url(r'^jiegua/$', views.Jiegua.as_view(), name='jiegua'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
