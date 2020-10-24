from django.urls import path

from . import views

app_name='EventViewApp'

urlpatterns = [
    path('', views.event_view, name='event_view'),
    path('calendar', views.event_calendar, name='event_calendar'),
    path('achive', views.event_view_achive, name='event_view_achive'),
    path('add', views.event_add, name='event_add'),
    path('ajax_get', views.ajax_get_event, name='ajax_get_event'),
    path('<int:event_id>/edit', views.event_edit, name='event_edit'),
    path('<int:event_id>/delete', views.event_delete, name='event_delete'),
    path('<int:event_id>/save', views.event_edit, name='event_save')
]