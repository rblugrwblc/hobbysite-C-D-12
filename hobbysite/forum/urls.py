from django.urls import path
from .views import post_list, post_detail

app_name = "forum"

urlpatterns = [
    path('threads/', post_list, name="list_view"),
    path('thread/<int:post_id>/', post_detail, name="detail_view"),
]