from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Commits
from .serializers import PostSerializer, CommitsSerializer
from .permissions import IsCreatorOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    Permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]

    # def get_serializer_class(self, *args, **kwargs):
    #     serializer = super().get_serializer_class()
    #     if self.request.method not in SAFE_METHODS:
    #         return CreatePostSerializer

    #     return serializer


    def perform_create(self, serializer):
        serializer.save(creator = self.request.user)


    @action(['PATCH'], True, permission_classes=[IsAuthenticated])
    def like(self, request, pk):
        post = self.get_object()

        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        serializer = self.get_serializer(post)
        return Response(serializer.data)

    @action(['POST'], True, permission_classes=[IsAuthenticated])
    def commits(self, request, pk):
        post = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save(creator=self.request.user, post=post)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED, headers=headers)


    
class CommitsViewSet(viewsets.ModelViewSet):
    queryset = Commits.objects.all()
    serializer_class = CommitsSerializer
    Permission_classes = [IsAuthenticated]
    # Permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator = self.request.user)

    # return Response(serializer.data)