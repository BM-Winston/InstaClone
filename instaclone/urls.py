from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns=[
    url('signup/',views.images,name = 'images'),
    url('^$', views.signup, name='signup'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),
    url('account/', include('django.contrib.auth.urls')), 
    url('add_post/', views.add_post, name='add_post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)