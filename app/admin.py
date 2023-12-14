from django.contrib import admin
from .models import (Speciality, Course, Module, Lesson, LessonPart, Task, Teacher, Oferta, OfertaContent)
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'show_question', 'difficulty', 'status']
    list_display_links = ['id', 'show_question', 'difficulty', 'status']
    list_filter = ['difficulty', 'status']

    def show_question(self, obj):
        return obj.question[:30]

@admin.register(Speciality)
class SpecialtyAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'title', 'slug', 'show_description', 'courses_count', 'members', 'status']
    list_display_links = ['id', 'title', 'slug', 'show_description', 'courses_count', 'members', 'status']
    search_fields = ['id', 'title', 'description']
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ['status', ]

    def show_description(self, obj):
        return obj.description[:30]

    def courses_count(self, obj):
        return obj.courses.all().count()

@admin.register(Course)
class CourseAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'title', 'slug', 'modules_count', 'education_type', 'members', 'status', 'created']
    list_display_links = ['id', 'title', 'slug', 'modules_count', 'education_type', 'members', 'status', 'created']
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ['created', 'status']
    ordering = ['id', ]

    def modules_count(self, obj):
        return obj.modules.all().count()

@admin.register(Module)
class ModuleAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'title', 'slug', 'lessons_count', 'teacher', 'price', 'support_day', 'members', 'status']
    list_display_links = ['id', 'title', 'slug', 'lessons_count', 'teacher', 'price', 'support_day', 'members', 'status']
    list_filter = ['status', ]
    prepopulated_fields = {'slug': ('title', )}
    ordering = ['id', ]

    def lessons_count(self, obj):
        return obj.lessons.all().count()

@admin.register(Lesson)
class LessonAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'title', 'slug', 'part_count', 'task_count', 'presentation_file', 'support_downloads',  'status', 'created']
    list_display_links = ['id', 'title', 'slug', 'part_count', 'task_count', 'presentation_file', 'support_downloads',  'status', 'created']
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ['status']

    def part_count(self, obj):
        return obj.part.all().count()

    def task_count(self, obj):
        return obj.task.all().count()

@admin.register(LessonPart)
class LessonPartAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'video', 'slug', 'status']
    list_display_links = ['id', 'title', 'video', 'slug', 'status']
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Teacher)
class TeacherAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'full_name', 'slug', 'image', 'degree', 'date_birth']
    list_display_links = ['id', 'full_name', 'slug', 'image', 'degree', 'date_birth']
    search_fields = ['full_name', 'company']
    prepopulated_fields = {'slug': ('full_name', )}
    list_filter = ['degree', ]

    def show_imge(self, obj):
        return obj.image.url

@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'oferta_content_count', 'created', 'updated']
    list_display_links = ['id', 'title', 'oferta_content_count', 'created', 'updated']

    def oferta_content_count(self, obj):
        return obj.oferta_content.all().count()

@admin.register(OfertaContent)
class OfertaContentAdmin(ImportExportActionModelAdmin):
    list_display = ['id',  'show_content', 'created', 'updated']
    list_display_links = ['id', 'show_content', 'created', 'updated']

    def show_content(self, obj):
        return obj.content.split('.')[0]