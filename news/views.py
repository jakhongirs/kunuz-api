from django.shortcuts import render
from .models import News
from .serializers import NewsSerializer
from rest_framework import generics
from helpers.pagination import CustomPagination


# Create your views here.
# ALL NEWS:
class AllNewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


class CategoryNewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug_name', None):
            queryset = queryset.filter(category__slug=self.kwargs['slug_name'])

        return queryset


class RegionNewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug_name', None):
            queryset = queryset.filter(region__slug=self.kwargs['slug_name'])

        return queryset


# IS_MAIN:
class IsMainNewsView(generics.ListAPIView):
    queryset = News.objects.filter(is_main=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_EDITOR_CHOICE:
class IsEditorChoiceNewsView(generics.ListAPIView):
    queryset = News.objects.filter(is_editor_choice=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_TREND:
class IsTrendNewsView(generics.ListAPIView):
    queryset = News.objects.filter(is_trend=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_INTERVIEW:
class IsInterviewView(generics.ListAPIView):
    queryset = News.objects.filter(is_interview=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_INVESTIGATION:
class IsInvestigationView(generics.ListAPIView):
    queryset = News.objects.filter(is_investigation=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_ARTICLE:
class IsArticleView(generics.ListAPIView):
    queryset = News.objects.filter(is_article=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_BUSINESS:
class IsBusinessView(generics.ListAPIView):
    queryset = News.objects.filter(is_business=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_VIDEONEWS:
class IsVideoNewsView(generics.ListAPIView):
    queryset = News.objects.filter(is_videonews=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_PHOTONEWS:
class IsPhotoNewsView(generics.ListAPIView):
    queryset = News.objects.filter(is_photonews=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# IS_ADVICED:
class IsAdvicedNewsView(generics.ListAPIView):
    queryset = News.objects.filter(is_adviced=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
