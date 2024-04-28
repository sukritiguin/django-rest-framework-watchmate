from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

"""
- Class Based Views
"""

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class StreamPlatformAV(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)
    

class StreamPlatformDetailsAV(APIView):
    def get(self, request, pk):
        try:
            strems = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        strem_serializer = StreamPlatformSerializer(strems, many=False, context={'request': request})
        return Response(strem_serializer.data)
    
    def put(self, request, pk):
        try:
            strems = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(instance=strems, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            strems = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        strems.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        movie_serializer = WatchListSerializer(movie, many=False)
        return Response(movie_serializer.data)
    
    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    
    


"""
- Function Based Views
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movies_serializer = MovieSerializer(movies, many=True)
        return Response(movies_serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        movie_serializer = MovieSerializer(movie, many=False)
        return Response(movie_serializer.data)
    if request.method == 'PUT':
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

"""