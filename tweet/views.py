from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .forms import TweetForm

class TweetListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = TweetForm()
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'tweet/tweet_list.html', {'form': form, 'tweets': tweets})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet:list')
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'tweet/tweet_list.html', {'form': form, 'tweets': tweets})
