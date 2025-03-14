from django.urls import path
from .views import post_list, post_detail

app_name = "forum"

urlpatterns = [
    path('threads/', post_list, name="post_list"),
    path('thread/<int:post_id>/', post_detail, name="post_detail"),
]

