from django.urls import path
from django.urls import include

urlpatterns = [
    path('api/', include('car_advisor_api.urls')),
]
