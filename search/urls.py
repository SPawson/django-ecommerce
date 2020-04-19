from django.conf.urls import url, include
from .views import do_Search

urlpatterns = [
    url(r'^$', do_Search, name='search'),
    
]