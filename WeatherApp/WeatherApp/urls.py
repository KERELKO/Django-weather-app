from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('WeatherApp.weather.urls', namespace='weather'))
]
