from django.db import models


class Link(models.Model):
    link_url = models.CharField(max_length=2083)  # Longest url possible in Chrome

    def __str__(self):
        return self.link_url
