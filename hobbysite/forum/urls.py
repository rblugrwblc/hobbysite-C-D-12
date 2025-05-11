from django.urls import path
from .views import thread_list, thread_detail, thread_create, thread_edit

app_name = "forum"

urlpatterns = [
    path('threads/', thread_list, name="list_view"),
    path('thread/<int:thread_id>/', thread_detail, name="detail_view"),
    path('thread/add/', thread_create, name='create_view'),
    path('thread/<int:thread_id>/edit/', thread_edit, name='edit_view'),
]