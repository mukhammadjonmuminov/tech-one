import uuid
from django.db.models import TextChoices

class SaveImages(object):

    """upload media files"""
    def teacher_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"app/image_gallery/teacher/{uuid.uuid4()}.{image_extension}"

    def work_company_logo(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"app/lesson/image_gallery/{uuid.uuid4()}.{image_extension}"

    def video_gallery_path(instance, filename):
        video_extension = filename.split('.')[-1]
        return f"app/lesson/video_gallery/{uuid.uuid4()}.{video_extension}"

    def presentation_file_path(instance, filename):
        file_extension = filename.split('.')[-1]
        return f"app/lesson/presentation_file/{uuid.uuid4()}.{file_extension}"

    def support_downloads_path(instance, filename):
            file_extension = filename.split('.')[-1]
            return f"app/lesson/support_downloads/{uuid.uuid4()}.{file_extension}"

class Status:
    class PublishRoles(TextChoices):
        DRAFT = 'df', 'Draft'
        PUBLISHED = 'pb', 'Published'

    class Difficulty(TextChoices):
        EASY = 'e', 'Easy'
        MEDIUM = 'm', 'Medium'
        HARD = 'h', 'Hard'

    class CourseRoles(TextChoices):
        ON = 'on', 'Online'
        OFF = 'off', 'Offline'