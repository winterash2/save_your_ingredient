from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StockSerializer
from .models import Stock
from rest_framework import permissions
from django.contrib.auth.decorators import login_required



class StockView(APIView):
    def get(self, request):
        queryset = Stock.objects.filter(user_id=request.user.id)
        print(request.user.id)
        # print(request)
        # print(request.data)
        # print(request.query_params)
        # print(request.parsers)
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data.update({"user_id":request.user.id})
        request.data._mutable = _mutable
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockDetailView(APIView):
    def get(self, request, stock_id):
        stock = Stock.objects.filter(id=stock_id)
        if stock:
            serializer = StockSerializer(stock, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error':"Can't find stock"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, stock_id):
        stock = Stock.objects.get(id=stock_id)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

# class StockView(viewsets.ModelViewSet):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
#     permisson_classes = (permissions.IsAuthenticated, )

#     def stock_create(self, serializer):
#         serializer.save(user=self.request.user, user_id=self.request.user)
