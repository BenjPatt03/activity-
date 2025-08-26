from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tweet
from django.utils import timezone
from django.contrib.auth.models import User
from history.models import History

@receiver(post_save, sender=Tweet)
def create_history_on_tweet_create(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        method = 'POST'
        tweet = instance
        date = timezone.now()
        summary = f"User {user.username} Created tweet with a content of '{tweet.content}' at {date.strftime('%Y-%m-%d %H:%M:%S')}"
        History.objects.create(user=user, method=method, tweet=tweet, date=date, summary=summary)

