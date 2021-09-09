from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Updates(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    news_img = models.ImageField(upload_to="images",default='testimon1.jpg.jpg')
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=15, null=True,blank=True)
    important = models.BooleanField(default=False)
    Tags = models.ManyToManyField(Tags, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering: ['-date_created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}{self.news_id}')
        super().save(*args, **kwargs)


