import uuid
from django.db.models import TextChoices

class SaveImages(object):
    def post_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"blog/post_images/{uuid.uuid4()}.{image_extension}"


class Status:
    class PublishRoles(TextChoices):
        DRAFT = 'df', 'Draft'
        PUBLISHED = 'pb', 'Published'