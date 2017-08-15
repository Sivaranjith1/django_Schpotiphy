from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [ 
                """url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),"""
                url(r'^$', views.home, name='home')
      
            ]
