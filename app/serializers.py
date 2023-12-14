from rest_framework import serializers
from .models import Teacher, Task, LessonPart, Lesson, Module, Course, Speciality

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'slug', 'image', 'degree', 'date_birth', 'work_company', 'work_company_logo']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'question', 'difficulty', 'status']

class LessonPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonPart
        fields = ['id', 'title', 'slug', 'video', 'status']

class LessonSerializer(serializers.ModelSerializer):
    part = LessonPartSerializer(many=True)
    task = TaskSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'slug', 'part', 'task', 'presentation_file', 'support_downloads', 'status', 'created']

class ModuleSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(many=True)
    teacher = TeacherSerializer()

    class Meta:
        model = Module
        fields = ['id', 'title', 'slug', 'lessons', 'teacher', 'price', 'support_day', 'members', 'status']

class CourseSerializer(serializers.ModelSerializer):

    modules = ModuleSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'modules', 'education_type', 'created', 'members', 'status']

class SpecialitySerializer(serializers.ModelSerializer):

    courses = CourseSerializer(many=True)

    class Meta:
        model = Speciality
        fields = ['id', 'title', 'slug', 'description', 'courses', 'members', 'status']