from django.views import View
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from .models import Speciality, Course, Module, Lesson, LessonPart, Task, Teacher, Oferta
from django.views.generic import CreateView, ListView, DetailView, DeleteView

class HomePageView(View):
    def get(self, request):
        speciality = Speciality.objects.all()
        courses = Course.objects.all()
        context = {
            "specialitys": speciality,
            "courses": courses,
        }
        return render(request, 'index.html', context)

class CoursesView(View):
    def get(self, request):
        speciality = Speciality.objects.all()
        courses = Course.objects.all()
        context = {
            "specialitys": speciality,
            "courses": courses,
        }
        return render(request, 'course.html', context)


class AboutPageView(ListView):
    model = Speciality
    template_name = 'about.html'
    context_object_name = 'specialitys'
    paginate_by = 10

# class CoursesView(ListView):
#     model = Course
#     template_name = 'course.html'
#     context_object_name = 'course'
#     paginate_by = 10

class TeachersView(ListView):
    model = Teacher
    template_name = 'teacher.html'
    context_object_name = 'teachers'
    paginate_by = 10

class OfertaDetailView(ListView):
    model = Oferta
    template_name = 'oferta/detail.html'
    context_object_name = 'offers'

