from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from .models import Todo
from .serializers import TodoListSerializer,RegisterSerializer,LogoutSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsOwner




# Create your views here.

class TodoViewSet(ModelViewSet):
   permission_classes = [IsAuthenticated,IsOwner]
   serializer_class = TodoListSerializer
   
   def get_queryset(self):
      if self.request.user.is_staff:
         return Todo.objects.all()
      
      return Todo.objects.filter(user = self.request.user)
   
   def perform_create(self, serializer):
      return serializer.save(user = self.request.user)


   filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
   filterset_fields = ['is_completed']
   search_fields = ['title', 'description']
   ordering_fields = ['create_at','title'] 


class RegisterView(APIView):
   def post(self,request):
      serializer = RegisterSerializer(data = request.data)

      if serializer.is_valid():
         serializer.save()
         return Response({'message':'User created'},status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)      
   

class LogoutView(APIView):
   permission_classes = [IsAuthenticated]

   def post(self,request):
      serializer = LogoutSerializer(data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response({'message':'Logged out sucessfully'},status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
