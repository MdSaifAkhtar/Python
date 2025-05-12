from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.db.models import Q
from rest_framework.views import APIView



class UserListCreateAPIView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        name = request.GET.get('name', '')
        sort = request.GET.get('sort', '')
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 5))

        # Search by name
        if name:
            queryset = queryset.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )

        # Sorting
        if sort:
            queryset = queryset.order_by(sort)

        # Pagination
        start = (page - 1) * limit
        end = start + limit
        serializer = UserSerializer(queryset[start:end], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get_object(self, pk):
        return generics.get_object_or_404(User, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = {key: value for key, value in request.data.items() if key in ["first_name", "last_name", "age"]}
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response({}, status=status.HTTP_200_OK)
