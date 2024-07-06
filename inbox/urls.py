from django.urls import path
from . import views

app_name='inbox'

urlpatterns=[ 
    path('new/<int:item_pk>/', views.new_chat,name='new'), 
    path('<int:pk>/', views.detail,name='detail'), 
    path('', views.inbox,name='inbox'), 

]