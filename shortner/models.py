from django.db import models


class Link(models.Model):
    link_url = models.URLField(max_length=2083)  # Longest url possible in Chrome

    def __str__(self):
        return self.link_url


class ShortLink(models.Model):
    short_url = models.CharField(max_length=100)
    source_link = models.OneToOneField(Link, on_delete=models.CASCADE)

    def __str__(self):
        return self.source_link.link_url
