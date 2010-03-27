from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/tag/%s' % self.name

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    enabled = models.BooleanField(default=True, help_text='Uncheck to hide the post')
    dateCreated = models.DateField(auto_now_add=True)
    lastUpdated = models.DateField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique_for_date=True)

    tags = models.ManyToManyField(Tag)

    def tag_urls(self):
        return ["<a href='%s'>%s</a>" % (tag.get_absolute_url(), tag.name) for tag in self.tags.all()]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/blog/%d/%s/%s' % (self.date_created.year, str(self.date_created.month).zfill(2), self.slug)

    