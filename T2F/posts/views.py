from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from . models import Post, Group, Comment, Like
from . forms import PostForm, UserForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from . import mixins
from django.http import HttpResponseRedirect

User = get_user_model()


def paginate(self, queryset):
    paginator = Paginator(queryset, settings.PAGINATION)
    page_number = self.request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = '-pub_date'
    paginate_by = settings.PAGINATION


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = (
            self.object.comments.select_related('author')
        )
        context['user_liked_post'] = Like.objects.filter(
            post=self.object, author=self.request.user).exists()
        return context


class PostUpdateView(mixins.OnlyAuthorMixin,
                     mixins.GetUrlPostDetailMixin,
                     UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'
    pk_url_kwarg = 'post_id'

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse(
            'posts:detail',
            kwargs={'post_id': self.kwargs['post_id']}))


class PostDeleteView(mixins.OnlyAuthorMixin,
                     mixins.GetUrlProfileMixin,
                     DeleteView):
    model = Post
    template_name = 'posts/create_post.html'
    pk_url_kwarg = 'post_id'


class PostCreateView(LoginRequiredMixin,
                     mixins.GetUrlProfileMixin,
                     CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class GroupDetailView(DetailView):
    model = Group
    template_name = 'posts/group_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = paginate(self, self.object.posts.all())
        return context


class GroupListView(ListView):
    model = Group
    template_name = 'posts/group_list.html'
    paginate_by = settings.PAGINATION


class ProfileDetailView(DetailView):
    template_name = 'posts/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.object.posts.order_by('-pub_date')
        context['page_obj'] = paginate(self, posts)
        context['posts_count'] = posts.count()
        return context


class ProfileUpdateView(LoginRequiredMixin,
                        mixins.GetUrlProfileMixin,
                        UpdateView):
    form_class = UserForm
    template_name = 'posts/user.html'

    def get_object(self):
        return self.request.user


class CommentCreateView(mixins.GetUrlPostDetailMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)


class CommentDeleteView(mixins.OnlyAuthorMixin,
                        mixins.GetUrlPostDetailMixin,
                        DeleteView):
    model = Comment
    template_name = 'posts/comment.html'
    pk_url_kwarg = 'comment_id'


class CommentUpdateView(mixins.OnlyAuthorMixin,
                        mixins.GetUrlPostDetailMixin,
                        UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment.html'
    pk_url_kwarg = 'comment_id'


class LikeCreateView(mixins.GetUrlPostDetailMixin, CreateView):
    model = Like
    fields = ()

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)


class LikeDeleteView(mixins.OnlyAuthorMixin,
                     mixins.GetUrlPostDetailMixin,
                     DeleteView):
    model = Like

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return get_object_or_404(Like, post=post, author=self.request.user)
