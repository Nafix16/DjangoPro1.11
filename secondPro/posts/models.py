from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=250, default=None)
    salary = models.IntegerField(default=None)

    class Meta:
        ordering = ('salary',)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)


def upload_location(instance, filename):
    return "%s/%s"%(instance.id, filename)


class Post(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    title = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='media/',
                              width_field="width",
                              height_field="height",
                              default=None, null=True)
    width = models.IntegerField(default=0, null=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    height = models.IntegerField(default=0, null=True)
    contents = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("id_detail", kwargs={"id": self.id})
