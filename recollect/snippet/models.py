from __future__ import unicode_literals
from django.db import models
from django.conf import settings

from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _



class Snippet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=10000)
    categories = models.CharField(max_length=250)
    language = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Snippet")
        verbose_name_plural = _("Snippets")
    
    def __unicode__(self):
        return smart_unicode(self.name)