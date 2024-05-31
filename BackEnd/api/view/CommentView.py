from rest_framework import viewsets, permissions, serializers

from api.model.CommentModel import Comment
from api.serializers.CommentSerializer import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer