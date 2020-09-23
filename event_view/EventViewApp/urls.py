from django.urls import path

from . import views

urlpatterns = [
    path('', views.event_view, name='event_view'),
    path('<int:event_id>/edit', views.event_edit, name='event_edit'),
    path('<int:event_id>/save', views.event_edit, name='event_save')
]
