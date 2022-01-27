from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cast',views.cast,name='cast'),
    path('query',views.query,name='query'),
    
]
