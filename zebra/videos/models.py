import uuid
from django.db import models
from storages.backends.s3boto import S3BotoStorage


def s3_file_name(instance, filename):
    return filename


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Video(BaseModel):
    url = models.URLField()
    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=256, blank=True)
    duration = models.TimeField(blank=True)

    file = models.FileField(
        null=True, blank=True, storage=S3BotoStorage(bucket="zebra-video")
    )  # upload_to=s3_file_name,

    # Add meta data
    # audio
    # audio = models.ForeignKey()
    # Frames


# class Audio(BaseModel):
#     video = models.OneToOneField(Video, on_delete=models.CASCADE)
#     file = models.FileField(
#         null=True, blank=True, storage=S3BotoStorage(bucket="zebra-audio")
#     )  # upload_to=s3_file_name,
#     is_transcribed = models.BooleanField(default=False)


# class Frame(BaseModel):
#     id = models.AutoField(primary_key=False, editable=False)
#     file = models.FileField(
#         null=True, blank=True, storage=S3BotoStorage(bucket="zebra-image")
#     )  # upload_to=s3_file_name,
#     video = models.ForeignKey(Video, related_name="frames")
#     is_processed = models.BooleanField(default=False)


# class Transcript(BaseModel):
#     pass
