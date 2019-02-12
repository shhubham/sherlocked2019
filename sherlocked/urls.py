from django.urls import path
from .import views

app_name='accounts'

urlpatterns=[
    path('signup/', views.signup_view, name='signup'),
    path('log/', views.log_view, name='log'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.homepage, name='homepage'),


    #url(r'^login/',views.login_view, name="login")
]
