from django.urls import path
from rango import views

urlpatterns = [
    path(r'about/',views.about, name='about'),
    path(r'',views.index, name='index'),
]
