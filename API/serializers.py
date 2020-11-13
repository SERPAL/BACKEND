from rest_framework import serializers

from .models import User
from .models import Book
from .models import Comment
from .models import Rating
from .models import Reviews
from .models import Messages

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'surname', 'password', 'image', 'email')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('user', 'name', 'pages', 'date', 'author2','description')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'content','date')

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'book','rate')

class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = ('user', 'book', 'content','date')

class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = ('user_from', 'user_to', 'message', 'created_at')