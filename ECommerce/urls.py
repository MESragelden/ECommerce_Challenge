from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url(r'^machines$', views.get_machines),
    url(r'^pods$', views.get_pods),
    url(r'^fill_database', views.fill_database),
]