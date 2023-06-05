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

    class Mata:
        db_table = 'tags'
        ordering = ['-id']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag of Music'
        indexes = [
        models.Index(fields=['tag']), 
    ]
    
    def __str__(self):
        return self.tag

class Type(BaseModel):
    type_of_music = models.CharField(max_length=255, null=False, blank=False)
    
    class Mata:
        db_table = 'types'
        ordering = ['-id']
        verbose_name = 'Type'
        verbose_name_plural = 'Type of Music'
        indexes = [
        models.Index(fields=['type_of_music']), 
    ]
    
    def __str__(self):
        return self.type_of_music

class Info(BaseModel):
    composer = models.CharField(max_length=255, null=True, blank=True)
    lyricist = models.CharField(max_length=255, null=True, blank=True)
    songwriter = models.CharField(max_length=255, null=True, blank=True)
    used_by = models.CharField(max_length=255, null=True, blank=True)

    class Mata:
        db_table = 'infos'
        ordering = ['-id']
        verbose_name = 'Information'
        verbose_name_plural = 'Information of Music'
        indexes = [
        models.Index(fields=['composer']),
        models.Index(fields=['composer', 'lyricist'])
    ]
    
    def __str__(self):
        return f'{self.composer}-{self.lyricist}-{self.songwriter}'
    

class Music(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    thumbnail = models.URLField(max_length=500, default='https://alcoholproject.blob.core.windows.net/mankind/capture_image_2022-12-27_17:31:58_893082.png')
    music = models.URLField(max_length=500, null=False, blank=False)
    lyricis = models.URLField(max_length=500, null=True, blank=True)
    info_id = models.OneToOneField(Info, on_delete=models.CASCADE)
    tag_id = models.ManyToManyField(Tag)
    type_of_music_id = models.ManyToManyField(Type)

    class Mata:
        db_table = 'musics'
        ordering = ['-id']
        verbose_name = 'Music'
        verbose_name_plural = 'Music Library'
        indexes = [
        models.Index(fields=['name']),
        models.Index(fields=['name', 'info_id', 'tag_id', 'type_of_music_id'])
    ]
    
    def __str__(self):
        return f'{self.name}'