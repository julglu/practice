from django.db import models
from datetime import datetime
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Author(models.Model):
    first_name=models.CharField('Name', max_length=32)
    last_name=models.CharField('Surname', max_length=32)
    email=models.EmailField('Email', null=True)
    birthyear=models.IntegerField('Birth year', null=True)

    def __unicode__(self):
        return u'%s %s.' %(
            self.last_name, self.first_name)

    def get_absolute_url(self):
        return "%i/" % self.id


class Book(models.Model):
    title=models.CharField('Title', max_length=128)
    authors=models.ManyToManyField('Author')
    publisher=models.ForeignKey('Publisher')
    publication_date=models.DateField('Date of publishing', default=datetime.now)

    def __unicode__(self):
        return u'%s' %(
            self.title)

    def get_absolute_url(self):
        return "%i/" % self.id


class Publisher(models.Model):
    title=models.CharField('Title', max_length=32)
    address=models.TextField('Address')
    city=models.CharField('City', max_length=64)
    country=models.CharField('Country', max_length=64)
    website=models.URLField('Website')

    def __unicode__(self):
        return u'%s (%s, %s)' %(
            self.title, self.city, self.country)


class BooksImage(models.Model):
    small_cover=models.ImageField(upload_to='books_images/small')
    zoomed_cover=models.ImageField(upload_to='books_images/zoomed', null=True, blank=True)
    book=models.ForeignKey('Book')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    def __unicode__(self):
        return u'%s' % self.book

    def images_cnt(self):
        cnt=0
        if self.small_cover:
            cnt+=1
        if self.zoomed_cover:
            cnt+=1
        return(cnt)

    def cover(self):
        if self.small_cover:
            return '<img src="%s">' %(self.small_cover.url)
        return None

    cover.allow_tags=True
