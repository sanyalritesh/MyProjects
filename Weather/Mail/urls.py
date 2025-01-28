
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

app_name = 'Mail'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendmail', views.Send_mail),

]