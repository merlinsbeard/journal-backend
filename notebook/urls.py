from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^page/(?P<slug>[-\w]+)/$', views.PageDetail.as_view()),
    url(r'^page/$', views.PageList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
