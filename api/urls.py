from django.urls import path, include
from . import views

urlpatterns = [
    path('mood/', views.ListMood.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls'))
]