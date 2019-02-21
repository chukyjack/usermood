from django.urls import path, include
from . import views

urlpatterns = [
    path('mood/', views.ListMood.as_view()),
    # path('mood/', views.mood_list, name='mood_list'),
    path('rest-auth/', include('rest_auth.urls')),
    # url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
]