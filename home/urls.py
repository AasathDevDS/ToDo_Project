from django.urls import path
from . import views

urlpatterns = [
  path('addTask/', views.addTask, name = "addTask" ),
  path('mark_as_read/<int:pk>', views.mark_as_read, name = 'mark_as_read'),
  path('delete/<int:pk>', views.delete, name = 'delete'),
  path('mark_as_unread/<int:pk>', views.mark_as_unread, name = 'mark_as_unread'),
  path('edit_task/<int:pk>', views.edit_task, name = 'edit_task'),
]