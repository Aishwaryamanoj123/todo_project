from django.urls import path
from . import views


urlpatterns = [
    path('',views.hello),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('delete/<int:task_id>/',views.delete_task, name='delete_task'),
    path('update/<int:id>/',views.update,name='update'),
    
]