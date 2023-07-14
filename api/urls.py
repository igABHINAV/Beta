from django.urls import path
from . import views
urlpatterns = [
    path('', views.send_request , name='requests'),
    path('deploy/' , views.index , name='index'),
]
