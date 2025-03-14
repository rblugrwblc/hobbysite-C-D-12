from django.urls import path
from .views import PostListView, PostDetailedView

app_name = "forum"

urlpatterns = [
    path('threads/', PostListView, name="list_view"),
    path('thread/<int:post_id>/', PostDetailedView, name="detail_view"),
]

