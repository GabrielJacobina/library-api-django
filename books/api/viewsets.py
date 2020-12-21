from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()