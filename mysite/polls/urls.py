from unicodedata import name
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register' ),
        path('tokenmsg',views.tokenmsg,name='tokenmsg' ),
        path('varified',views.varifiedmsg,name='varified'),
        path('verify/<token>/',views.verify,name="verify"),
        path('error',views.error,name='error'),
        path('login',views.logins,name='login'),
        path('logout',views.logoutpage,name="logout"),
        path('forget_password',views.forget_pass,name='forget'),
 
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),


]