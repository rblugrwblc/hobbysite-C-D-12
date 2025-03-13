from django.urls import path
from .views import PostListView, PostDetailedView

app_name = "forum"

urlpatterns = [
    path('threads/', PostListView, name="post_list"),
    path('thread/<int:post_id>/', PostDetailedView, name="post_detail"),
]

