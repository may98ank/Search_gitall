from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.SearchHome, name = "search_home"),
    url(r'^result', views.find, name = "search_result"),
]
