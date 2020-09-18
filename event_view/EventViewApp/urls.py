from django.urls import path

from . import views

urlpatterns = [
    path('', views.event_view, name='event_view'),
    path('edit', views.event_edit, name='event_edit')
]
