from django.contrib import admin
from django.urls import path
from forecast_app.views import forecast_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', forecast_view, name='forecast'),
]
