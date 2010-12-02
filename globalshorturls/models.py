from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Shorturl(models.Model):
    """
        Shorturl model
    """
    url = models.CharField(max_length=200)
    shorturl = models.CharField(max_length=200)
    creator = models.ForeignKey(User, verbose_name='creator',)
    counter = models.IntegerField(default = 0,)

    def __unicode__(self):
        return self.url
        
class ShorturlForm(ModelForm):
    class Meta:
        model = Shorturl
        fields = ('url',)
