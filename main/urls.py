from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('notify/', views.notify, name = 'notify')
]