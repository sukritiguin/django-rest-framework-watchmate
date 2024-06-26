"""
URL configuration for watchmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path("list/", views.WatchListAV.as_view(), name='list'),
    path("list/<int:pk>/", views.WatchDetailsAV.as_view(), name='"watchlist-detail'),

    path('', include(router.urls)),
    # path("stream/", views.StreamPlatformAV.as_view(), name='stream'),
    # path("stream/<int:pk>/", views.StreamPlatformDetailsAV.as_view(), name='streamplatform-detail'),

    # path('review/', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),

    path('stream/<int:pk>/review/', views.ReviewList.as_view(), name='review-list'),
    path('stream/<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('stream/review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]
