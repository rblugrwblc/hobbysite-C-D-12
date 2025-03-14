from django.urls import path
from .views import commission_list, commission_detail


urlpatterns = [
    path('list/', commission_list, name='list_view'),
    path('detail/<int:pk>/', commission_detail, name='detail_view'),
]

app_name = 'commissions'
