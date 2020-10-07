from django.urls import path

from . import views

app_name='EventViewApp'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'), #追加
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('', views.event_view, name='event_view'),
    path('achive', views.event_view_achive, name='event_view_achive'),
    path('add', views.event_add, name='event_add'),
    path('<int:event_id>/edit', views.event_edit, name='event_edit'),
    path('<int:event_id>/delete', views.event_delete, name='event_delete'),
    path('<int:event_id>/save', views.event_edit, name='event_save')
]
