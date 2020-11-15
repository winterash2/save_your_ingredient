from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailSerializer, ExperienceRecipeSerializer
from .models import UserDetail, ExperienceRecipe
from recipe.models import Recipe
from rest_framework import permissions
from django.shortcuts import get_object_or_404
# Create your views here.


class UserDetailView(APIView):
    def get(self, request):
        try:
            # user_detail = get_object_or_404(UserDetail, user=request.user)
            user_detail = UserDetail.objects.filter(user=request.user)
        except:
            user_detail = UserDetail()
            user_detail.user = request.user
            user_detail.total_time = 0
            user_detail.save()
            user_detail = UserDetail.objects.filter(user=request.user)

        serializer = UserDetailSerializer(user_detail, many=True)
        # print(serializer.data)
        return Response(serializer.data)
