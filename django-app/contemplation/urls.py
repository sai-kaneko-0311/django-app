from django.conf.urls import url
from contemplation import views

urlpatterns = [
    url('', views.index, name='index'),
]