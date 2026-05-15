from tempfile import template

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "threads"
urlpatterns = [path("", views.index, name="index"),
               path('new_thread/', views.thread_create, name='create_thread'),
               path("register/", views.register, name="register"),
               path("login/", views.user_login, name="login"),
               path("logout/", views.user_logout, name="logout"),
               path("posts/<int:id>/", views.post_detail, name="post_detail"),
               path("profile/<int:id>/", views.profile_detail, name="profile_detail")]

               # path("login/", auth_views.LoginView.as_view(template_name="threads/login.html"), name="login"),
               # path("login/", auth_views.LogoutView.as_view(template_name="registration/loggedout.html"), name="logout")]
