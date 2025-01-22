from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchApiView.as_view(), name="search"),
    path('contents/', views.ContentListView.as_view(), name="contents"),
]
