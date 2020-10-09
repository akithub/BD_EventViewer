from django.urls import path

from . import views

app_name='EventViewApp'

urlpatterns = [
    path('', views.event_view, name='event_view'),
    path('achive', views.event_view_achive, name='event_view_achive'),
    path('add', views.event_add, name='event_add'),
    path('<int:event_id>/edit', views.event_edit, name='event_edit'),
    path('<int:event_id>/delete', views.event_delete, name='event_delete'),
    path('<int:event_id>/save', views.event_edit, name='event_save')
]