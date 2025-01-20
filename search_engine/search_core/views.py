from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SearchQuerySerializer

# Create your views here.


# def hello_search(request):
#     return JsonResponse({
#         "message" : "Hi this search page ",
#         "status" : "active"
#     })


class SearchApiView(APIView):
    def get(self, request):
        return Response({
            "message" : "search Page Api ",
            "status" : "active",
        })
        
        
    def post(self , request):
        serializer = SearchQuerySerializer(data = request.data)
        if serializer.is_valid():
            # your search Logic Here
            return Response({
                "message" : "Search Executed",
                "data" : serializer.validated_data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)