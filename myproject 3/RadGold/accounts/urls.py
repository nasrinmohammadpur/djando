from django.urls import path
from  accounts import views
 
 
urlpatterns = [
    path('', views.home, name='accounts' ),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name='signup'),
]