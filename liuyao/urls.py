from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.PaipanInput.as_view(), name='index'),
    url(r'^bagua/', views.PaipanResult.as_view(), name='paipan')
]

# urlpatterns = format_suffix_patterns(urlpatterns)
