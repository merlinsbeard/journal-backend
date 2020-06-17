from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('notebook.urls')),
    path('v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]
