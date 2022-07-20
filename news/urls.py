from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.AllNewsView.as_view(), name="all_news"),
    path('news/category/<slug:slug_name>/', views.CategoryNewsView.as_view()),
    path('news/main/', views.IsMainNewsView.as_view(), name="is_main"),
    path('news/editor-choice/', views.IsEditorChoiceNewsView.as_view(), name="is_editor_choice"),
    path('news/trend/', views.IsTrendNewsView.as_view(), name="is_trend"),
    path('interview/', views.IsInterviewView.as_view(), name="is_interview"),
    path('news/surishtiruv/', views.IsInvestigationView.as_view(), name="is_investigation"),
    path('articles/', views.IsArticleView.as_view(), name="is_article"),
    path('business/', views.IsBusinessView.as_view(), name="is_business"),
    path('news/videonews', views.IsVideoNewsView.as_view(), name="is_videonews"),
    path('news/photonews', views.IsPhotoNewsView.as_view(), name="is_photonews"),
]
