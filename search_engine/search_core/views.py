

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContentSerializer
from .models import Content
from django.db.models import Q
# Create your views here.


# def hello_search(request):
#     return JsonResponse({
#         "message" : "Hi this search page ",
#         "status" : "active"
#     })


class SearchApiView(APIView):
    def get(self, request):
        query = request.query_params.get('q', "")
        if query:
            result = Content.objects.filter(
                Q(title_icontains=query)|
                Q(content_icontains = query)
            )
            serializer =ContentSerializer(result, many=True)
            return Response({
                "count" : len(serializer.data),
                "result" : serializer.data,
            })
            
        return Response({
            "message": "Please provide a search query",
            "example": "/api/search/?q=your_search_term"
        })
        
        
    def post(self , request):
        serializer = ContentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # your search Logic Here
            return Response({
                "message" : "content create successfully",
                "data" : serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)