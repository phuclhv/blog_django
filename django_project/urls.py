"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# import those to include the urls file of other applications
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static  
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Since this is the highest level urls file of the page, we has to include all the urls file of the apps contained.
    # this line will map to urls.py file in folder blog
    path('', include('blog.urls')),
    
    # Instead of creating the new urls file in the app using "include"
    # We can import directly to the project url
    path('register/',user_views.register, name='register') ,
    path('profile/',user_views.profile, name='profile'),

    # We need to define the template_name to overide the default one
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     
