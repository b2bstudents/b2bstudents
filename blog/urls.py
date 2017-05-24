from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^accueil/(?P<pseudo>[-\w]+)$', views.acc, name="accueil"),
    url(r'^vente$', views.vente),
    url(r'^base$', views.base),
    url(r'^inscription$', views.inscr, name="inscription"),
    url(r'^login$', views.login, name="login"),
    url(r'^article/(?P<id_article>\d+)/(?P<id_user>\d+)$', views.view_article, name="afficher_article"),
    url(r'^logout$', views.logot, name="logot"),
]
