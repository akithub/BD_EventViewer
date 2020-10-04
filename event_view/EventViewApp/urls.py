from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('', views.event_view, name='event_view'),
    path('add', views.event_add, name='event_add'),
    path('<int:event_id>/edit', views.event_edit, name='event_edit'),
    path('<int:event_id>/delete', views.event_delete, name='event_delete'),
    path('<int:event_id>/save', views.event_edit, name='event_save')
]
