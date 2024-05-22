from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # logowanie i rejestracja
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # autoryzacja logowania
    path('blog/login/', auth_views.LoginView.as_view(), name='blog_login'),
    path('blog/logout/', auth_views.LogoutView.as_view(), name='blog_logout'),
    path('blog/signup/', views.signup, name='blog_signup'),

    path('account/', views.account_settings, name='account_settings'),
]