from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [
                url(r'^$', views.home, name='home'),
                url(r'^genre/$', views.GenreList.as_view(),
                    name='genre'),
                url(r'^genre/(?P<sjanger_id>[0-9]+)/', views.genreView, name='genreView'),
                url(r'^songs/(?P<sang_id>[0-9]+)/', views.play, name='sangen')
      
            ]
