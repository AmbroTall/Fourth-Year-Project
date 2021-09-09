from django.db import models
from django.template.defaultfilters import slugify



class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Houses(models.Model):
    house_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tags, null=True, blank=True)
    house_img = models.ImageField(upload_to="images", default='house3.jpg')
    slug = models.SlugField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        ordering: ['-date_created']


    def __str__(self):
        return self.location

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.location}')
        super(Houses, self).save(*args, **kwargs)