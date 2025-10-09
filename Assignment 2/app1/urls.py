from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_video', views.add_video, name='add_video'),
    path('list', views.list_videos, name='list_videos'),
    path('edit/<int:pk>', views.edit_video, name='edit_video'),
    path('delete/<int:pk>', views.delete_video, name='delete_video'),
    path('report', views.report_video, name='report_video'),
]