from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('Фото', upload_to='posts_images', blank=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(verbose_name='Введите текст комментария:')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date', )
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        unique_together = ('post', 'author')
        verbose_name = 'лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f"Like by {self.author} on {self.post}"
