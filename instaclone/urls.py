from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.hello,name = 'hello'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)