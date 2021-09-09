from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Projects(models.Model):
    proj_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    proj_img = models.ImageField(upload_to="images",default='images_1.jpg')
    body = RichTextUploadingField()
    project_by = models.CharField(max_length=50)
    date_published = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    class Meta:
        ordering: ['-date_published']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}{self.proj_id}')
        super(Projects, self).save(*args, **kwargs)

