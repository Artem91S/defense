from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetDataUser.as_view(), name='home'),
    path('success', views.success, name='success'),
    path('unsuccess', views.unsuccess, name='unsuccess')
]