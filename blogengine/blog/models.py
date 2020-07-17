from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from time import time


def gen_slug(title):
    new_slug = slugify(title, allow_unicode=True)
    return new_slug + "-" + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('post_edit_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_details', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('tag_edit_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
