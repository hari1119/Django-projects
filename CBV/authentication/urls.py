from django.urls import path  
from . import views


urlpatterns = [  
    path('', views.index),
    path('test/', views.signin),
    path('logout/', views.signout,name='logout'),
    path('signup/', views.signup),  
    path('mail/',views.mail),
    path('tasks/', views.display_tasks, name='display_tasks'),
    path('tasks/<int:id>/delete/', views.delete_task, name='delete_task'),
]

