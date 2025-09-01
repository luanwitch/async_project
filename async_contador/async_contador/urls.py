from django.contrib import admin
from django.urls import path
from contador_async_final.views import contador_view  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contador_view),     
    path('contador/', contador_view),
]
