from django.contrib import admin
from django.urls import path, include
from dcrm import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),  # include your app's urls
    path('accounts/', include('django.contrib.auth.urls')),  # include the auth urls
    path('', views.index, name='home'),  # Update the name here to 'home'
]
