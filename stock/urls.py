from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StockView

stock_list = StockView.as_view({
    'post': 'create',
    'get': 'list'
})

stock_detail = StockView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('stock/', stock_list, name='stock_list'),
    path('stock/<int:pk>/', stock_detail, name='stock_detail'),
])
