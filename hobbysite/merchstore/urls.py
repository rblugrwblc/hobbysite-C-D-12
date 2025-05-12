from django.urls import path
from .views import item, item_list, item_add, item_edit, merch_cart, merch_transactions

urlpatterns = [
    path('item/<int:id>/', item, name='detail_view'),
    path('items/', item_list, name='list_view'),
    path('item/add/', item_add, name='add_view'),
    path('item/<int:id>/edit/', item_edit, name='edit_view'),
    path('cart/', merch_cart, name='cart_view'),
    path('transactions/', merch_transactions, name='transactions_view'),
]

app_name = "merchstore"
