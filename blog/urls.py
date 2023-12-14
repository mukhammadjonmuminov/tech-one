from django.urls import path
from .views import BlogListView, BlogDetailView, ContactView

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('single/', BlogDetailView.as_view(), name='single'),
    path('contact/', ContactView.as_view(), name='contact'),
]