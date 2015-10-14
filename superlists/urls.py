from django.conf.urls import include, url
from lists import views as list_views
from lists import urls as list_urls
from blog import views as blog_views

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
    url(r'^blog/', blog_views.blog_page, name='blog'),
]
