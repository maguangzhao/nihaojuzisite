from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'',views.JuZiListView.as_view(),name='juzilist'),
    url(r'^juzi/',views.JuZiListView.as_view(),name='juzilist'),
    url(r'^book/',views.JuZiListView.as_view(),name='booklist'),
    url(r'^movie/',views.JuZiListView.as_view(),name='movielist')
]