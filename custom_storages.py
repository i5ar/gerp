from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticS3Boto3Storage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaS3Boto3Storage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
