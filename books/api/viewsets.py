from rest_framwork import viewsets
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.BooksSerializer
    queryset = models.Books.all()