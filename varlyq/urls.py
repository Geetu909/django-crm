# varlyq/urls.py

from django.contrib import admin
from django.urls import path
from dcrm import views
from dcrm.views import index, home, login_user, logout_user, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    
    path('accounts/login/', views.index, name='home'),  # Home page URL
    path('home/', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
    path('add_record/', views.add_record, name='add_record'),
]
