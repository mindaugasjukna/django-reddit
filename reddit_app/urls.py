from django.urls import path
from . import views

app_name = 'reddit_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('change_status', views.change_status, name="change_status"),
    path('delete_post', views.delete_post, name="delete_post")
]
