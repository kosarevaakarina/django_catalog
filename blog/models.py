from django.db import models
from django.urls import reverse
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=150, verbose_name='Человекопонятный URL', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    create_date = models.DateField(verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    count_of_view = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def delete(self, *args, **kwargs):
        self.is_published = False
        self.save()

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ('title',)
