from django.shortcuts import render
# Create your views here.
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(GenericViewSet, CreateModelMixin,ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
      serializer_class = UserSerializer
      queryset = User.objects.all()

'''
      @api_view(['GET', 'POST'])
      def user_list(request):
          if request.method == 'GET':
              snippets = User.objects.all()
              serializer = UserSerializer(snippets, many=True)
              return Response(serializer.data)

          elif request.method == 'POST':
              serializer = UserSerializer(data=request.data)
              if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      @api_view(['GET', 'PUT', 'DELETE'])
      def user_detail(self, pk):
          try:
              user = User.objects.get(pk=pk)
          except User.DoesNotExist:
              return HttpResponse(status=404)

          if self.method == 'GET':
              serializer = UserSerializer(user)
              return JsonResponse(serializer.data)

          elif self.method == 'PUT':
              data = JSONParser().parse(self)
              serializer = UserSerializer(user, data=data)
              if serializer.is_valid():
                  serializer.save()
                  return JsonResponse(serializer.data)
              return JsonResponse(serializer.errors, status=400)

          elif self.method == 'DELETE':
              user.delete()
              return HttpResponse(status=204)
'''

