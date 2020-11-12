from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecipeSerializer
from .models import Recipe
from .recommend_recipe import recommend_ingredient, recommend_expiration_date


class RecipeExpirationAPIView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        result_dict = recommend_expiration_date()
        return Response(result_dict)


class RecipeStockAPIView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        result_dict = recommend_ingredient()
        return Response(result_dict)

