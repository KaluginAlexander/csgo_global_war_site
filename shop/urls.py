from django.urls import path
from shop import views

urlpatterns = [
    path('notify', views.notify, name = 'notify')
]