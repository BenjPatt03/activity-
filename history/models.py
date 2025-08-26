from django.db import models
from django.contrib.auth.models import User
from tweet.models import Tweet

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=10)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return f"{self.summary}"
