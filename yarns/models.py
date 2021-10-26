from django.db import models

from users.models import Blogger


def blogger_directory_path(instance, filename):
    """All uploads by a blogger should be in the same directory."""
    return f'blogger_{instance.blogger.pk}/{filename}'

class Yarn(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    upload = models.FileField(upload_to=blogger_directory_path, blank=True, null=True)
    parent_yarn = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(Blogger, related_name='likes', blank=True)
    re_yarn = models.ManyToManyField(Blogger, related_name='reyarn', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'yarn'
        verbose_name_plural = 'yarnings'
    
    @property
    def num_of_likes(self):
        return self.likes.count()
    
    @property
    def num_of_replies(self):
        return self.yarn_set.count()
    
    @property
    def num_of_reyarn(self):
        return self.re_yarn.count()
    
    @property
    def get_direct_replies(self):
        return self.yarn_set.filter(parent_yarn=self.id)
    