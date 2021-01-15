from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', views.LogoutView.as_view(next_page= '/')),
    path('tinymce/', include('tinymce.urls')),
]


