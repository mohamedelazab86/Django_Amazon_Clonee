from django.urls import path
from .views import ProductList,ProctDetail

urlpatterns=[
    path('',ProductList.as_view()),
    path('<slug:slug>',ProctDetail.as_view()),
]