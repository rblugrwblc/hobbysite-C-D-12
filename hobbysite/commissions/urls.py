from django.urls import path
from .views import CommissionCreateView, CommissionListView, CommissionUpdateView, CommissionDetailView, JobView


urlpatterns = [
    path('list/', CommissionListView.as_view(), name='list_view'),
    path('detail/<int:pk>/',CommissionDetailView.as_view(), name='detail_view',),
    path('<int:pk>/edit/', CommissionUpdateView.as_view(), name='update_commission'),
    path('add/', CommissionCreateView.as_view(), name='add_commission'),
    path('job/<int:pk>', JobView.as_view(), name='job_view'),
]

app_name = 'commissions'
