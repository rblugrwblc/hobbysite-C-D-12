from django.urls import path
from .views import item, item_list

urlpatterns = [
    path('merchstore/item/<int:id>/', item, name="detail_view"),
    path('merchstore/items/', item_list, name="list_view"),
]

app_name = "merchstore"
