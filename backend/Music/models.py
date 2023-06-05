from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')

    class Meta:
        abstract = True


class Tag(BaseModel):
    tag = models.CharField(max_length=255, null=False, blank=False)


class Type(BaseModel):
    type_of_music = models.CharField(max_length=255, null=False, blank=False)


class Info(BaseModel):
    composer = models.TextField(max_length=255, null=True, blank=True)
    lyricist = models.TextField(max_length=255, null=True, blank=True)
    songwriter = models.TextField(max_length=255, null=True, blank=True)
    used_by = models.TextField(max_length=255, null=True, blank=True)


class Music(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    thumbnail = models.URLField(max_length=500, default='https://alcoholproject.blob.core.windows.net/mankind/capture_image_2022-12-27_17:31:58_893082.png')
    music = models.URLField(max_length=500, null=False, blank=False)
    lyricis = models.URLField(max_length=500, null=True, blank=True)
    info_id = models.ForeignKey(Info, on_delete=models.CASCADE)
    tag_id = models.ManyToManyField(Tag)
    type_of_music_id = models.ManyToManyField(Type)