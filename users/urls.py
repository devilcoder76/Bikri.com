from django.urls import path
from . import views
app_name="users"

urlpatterns=[
    path('register/',views.reg_form,name="userform"),
    path('login/',views.login,name="login_User"),
    path('logout/',views.logout,name="logout_User"),
]