from django.urls import path
from .views import HomePageView, AboutPageView, CoursesView, TeachersView, OfertaDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('courses/', CoursesView.as_view(), name='courses'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('oferta/', OfertaDetailView.as_view(), name='oferta'),
]