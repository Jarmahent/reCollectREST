from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver



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

# Generate tokens for all existing users
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


# Give every new user a token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)