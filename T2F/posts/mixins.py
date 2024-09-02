from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin


class GetUrlPostDetailMixin:
    def get_success_url(self):
        return reverse('posts:detail',
                       kwargs={'post_id': self.kwargs['post_id']})


class GetUrlProfileMixin:
    def get_success_url(self):
        return reverse('posts:profile',
                       kwargs={'username': self.request.user.username})


class OnlyAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user
