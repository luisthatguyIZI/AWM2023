from django.urls import path
from .import views

urlpatterns= [
    path('',views.index,name='index'),
    path('charts/',views.charts,name='charts'),
    path('login/',views.login,name="login"),
    path('tables/',views.tables,name="tables")
]