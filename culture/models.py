from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify


class Culture(models.Model):
    culture_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images")
    description = models.CharField(max_length=100)
    body = RichTextUploadingField(max_length=2000)
    slug = models.SlugField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering: ['-date_created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}{self.culture_id}')
        super(Culture, self).save(*args, **kwargs)
