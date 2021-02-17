from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

class todo(Model):
    title = models.CharField(max_length = 100)
    memo = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null =True, blank = True)
    importent = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title