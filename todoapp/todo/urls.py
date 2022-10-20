from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_task/', views.add_task, name='create_task'),
    path('update_task/<pk>', views.task_update, name='update_task'),
    path('delete_task/<pk>', views.delete_task, name='delete_task'),
]
