from django.urls import path
from .views import index,list

urlpatterns = [
    path('', index ,name='index'),
    path('list',list,name='list' )
]