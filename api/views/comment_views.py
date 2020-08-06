from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.comment import Comment
from ..serializers import CommentSerializer

# Create your views here.
class Comments(APIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CommentSerializer
    def get(self, request):
        """Index Request"""
        print(request.session)
        comments = Comment.objects.all()[:10]
        # data = CommentReadSerializer(comments, many=True).data
        data = CommentSerializer(comments, many=True).data
        return Response(data)

    def post(self, request):
        """Post request"""
        print(request.data)
        comment = CommentSerializer(data=request.data['comment'])
        if comment.is_valid():
            b = comment.save()
            return Response(comment.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        comment = get_object_or_404(Comment, pk=pk)
        # data = CommentReadSerializer(comment).data
        data = CommentSerializer(comment).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        comment = get_object_or_404(Comment, pk=pk)
        ms = CommentSerializer(comment, data=request.data['comment'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
