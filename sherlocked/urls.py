from django.urls import path
from .import views

app_name='sherlock'

urlpatterns=[
    path('signup/', views.signup_view, name='signup'),
    path('log/', views.log_view, name='log'),
    #path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.homepage, name='homepage'),


    #url(r'^login/',views.login_view, name="login")
]
