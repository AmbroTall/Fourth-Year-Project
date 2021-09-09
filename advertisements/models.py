from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Advertisements(models.Model):
    advert_id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    advert_img = models.ImageField(upload_to="images")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    body = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(max_length=20,null=True, blank=True)
    home_advert = models.BooleanField(default=False)
    house_advert = models.BooleanField(default=False)
    news_advert = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering: ['-date_created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}{self.advert_id}')
        super(Advertisements, self).save(*args, **kwargs)