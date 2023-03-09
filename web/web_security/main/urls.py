from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_main, name='home'),
    path('calculator', views.index_calculator, name='calculator'),
    path('general_docs', views.index_general_docs, name='general_docs'),
    path('about', views.index_about, name='about'),
]
