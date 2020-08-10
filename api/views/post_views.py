from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.post import Post
from ..serializers import PostSerializer, PostReadSerializer, UserSerializer

# Create your views here.
class Posts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PostSerializer
    def get(self, request):
        """Index request"""
        posts = Post.objects.all()
        # posts = Post.objects.filter(owner=request.user.id)
        data = PostReadSerializer(posts, many=True).data
        return Response(data)


    def post(self, request):
        """Create request"""
        # Add user to request object
        request.data['post']['owner'] = request.user.id
        # Serialize/create post
        post = PostSerializer(data=request.data['post'])
        if post.is_valid():
            m = post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        post = get_object_or_404(Post, pk=pk)
        data = PostReadSerializer(post).data
        # Only want to show owned posts?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this post')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        post = get_object_or_404(Post, pk=pk)
        if not request.user.id == post.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this post')
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        if request.data['post'].get('owner', False):
            del request.data['post']['owner']

        # Locate Post
        post = get_object_or_404(Post, pk=pk)
        # Check if user is  the same
        if not request.user.id == post.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this post')

        # Add owner to data object now that we know this user owns the resource
        request.data['post']['owner'] = request.user.id
        # Validate updates with serializer
        ms = PostSerializer(post, data=request.data['post'])
        if ms.is_valid():
            ms.save()
            print(ms)
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
