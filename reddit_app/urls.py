from django.urls import path
from . import views
from .api import TodoList, TodoDetail

app_name = 'reddit_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('change_status', views.change_status, name="change_status"),
    path('delete_post', views.delete_post, name="delete_post"),
    path('api/v1/', TodoList.as_view()),
    path('api/v1/<int:pk>/', TodoDetail.as_view()),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
]
