from rest_framework import viewsets
from .serializers import StockSerializer
from .models import Stock
from rest_framework import permissions


class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permisson_classes = (permissions.IsAuthenticated, )

    def stock_create(self, serializer):
        serializer.save(user=self.request.user, user_id=self.request.user)
