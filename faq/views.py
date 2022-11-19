from django.shortcuts import render
from .models import FAQ, Category
from rest_framework import generics, status
from .models import FAQ
from .serializers import FAQSerializer

class FAQview(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer