from django.db import models




# Djumpstart Test
class HelloDjango(models.Model):
    title = models.CharField(max_length=200)


# Tutorial Examples
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


# Disable signal that creates super user after syncdb


#from django.db.models import signals
#from django.contrib.auth.management import create_superuser
#from django.contrib.auth import models as auth_app


#signals.post_syncdb.disconnect(
#    create_superuser,
#    sender=auth_app,
#    dispatch_uid = "django.contrib.auth.management.create_superuser")
