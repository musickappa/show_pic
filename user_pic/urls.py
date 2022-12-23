from django.urls import path

from .views import show_picdetail,show_piclist,register_pic,delete_pic,update_pic,profile


urlpatterns = [
    path('list/', show_piclist.as_view(), name='list'),
    path('detail/<int:pk>/', show_picdetail.as_view(), name='detail'),
    path('register/', register_pic.as_view(), name='register'),
    path('delete/<int:pk>/', delete_pic.as_view(), name='delete'),
    path('update/<int:pk>/', update_pic.as_view(), name='delete'),
    path('profile/<int:pk>/', profile.as_view(), name='profile'),
    
]