from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchApiView.as_view(), name="hello_search")
]
