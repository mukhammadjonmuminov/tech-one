from django.db import models
from .helpers import SaveImages, Status

class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to=SaveImages.teacher_images_path)
    degree = models.CharField(max_length=255)
    date_birth = models.DateField()
    # work_company = models.CharField(max_length=100)
    # work_company_logo = models.ImageField(upload_to=SaveImages.work_company_logo)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name

class Task(models.Model):
    question = models.TextField()
    difficulty = models.CharField(max_length=1, choices=Status.Difficulty.choices, default=Status.Difficulty.EASY)
    status = models.CharField(max_length=2, choices=Status.PublishRoles.choices, default=Status.PublishRoles.PUBLISHED)

    def __str__(self):
        return self.id

class LessonPart(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    video = models.FileField(upload_to=SaveImages.video_gallery_path)
    status = models.CharField(max_length=2, choices=Status.PublishRoles.choices, default=Status.PublishRoles.PUBLISHED)

    class Meta:
        ordering = ['id']
        verbose_name = 'Lesson Part'
        verbose_name_plural = 'Lesson Parts'

    def __str__(self):

        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    part = models.ManyToManyField(LessonPart, blank=True)
    task = models.ManyToManyField(Task, blank=True)
    presentation_file = models.FileField(upload_to=SaveImages.presentation_file_path, blank=True)
    support_downloads = models.FileField(upload_to=SaveImages.support_downloads_path, blank=True)
    status = models.CharField(max_length=2, choices=Status.PublishRoles.choices, default=Status.PublishRoles.PUBLISHED)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    lessons = models.ManyToManyField(Lesson, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField()
    support_day = models.PositiveIntegerField(default=45)
    members = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.PublishRoles.choices, default=Status.PublishRoles.PUBLISHED)

    class Meta:
        ordering = ['id']
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    modules = models.ManyToManyField(Module, blank=True)
    education_type = models.CharField(max_length=3, choices=Status.CourseRoles.choices, default=Status.CourseRoles.ON)
    created = models.DateField(auto_now_add=True)
    members = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.PublishRoles.choices, default=Status.PublishRoles.PUBLISHED)

    class Meta:
        ordering = ['id']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    @staticmethod
    def get_objects():
        return Course.objects.order_by('id')

    def __str__(self):
        return self.title

class Speciality(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True)
    members = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.PublishRoles.choices, default=Status.PublishRoles.PUBLISHED)

    class Meta:
        ordering = ['id']
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialitys'

    # @staticmethod
    # def get_objects():
    #     return Speciality.objects.order_by('id')

    def __str__(self):
        return self.title

class OfertaContent(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Oferta(models.Model):
    title = models.CharField(max_length=255)
    oferta_content = models.ManyToManyField(OfertaContent, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title