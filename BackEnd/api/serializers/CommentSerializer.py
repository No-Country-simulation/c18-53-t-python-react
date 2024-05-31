from rest_framework import serializers
from api.model.CommentModel import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['text','user','product']