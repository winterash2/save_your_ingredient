from django.urls import path, include
from .views import UserDetailView

urlpatterns = [
    path('user-detail/', UserDetailView.as_view(), name='user-detail'),
    # path('stock/<int:stock_id>/', StockDetailView.as_view(), name='stock_detail')
    # path('stock/<int:pk>/', stock_detail, name='stock_detail'),
]
