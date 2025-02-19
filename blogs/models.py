from django.db import models


class Blogs(models.Model):
    header = models.CharField(max_length=150, verbose_name="Заголовок блога", help_text="Введите заголовок блога")
    content = models.TextField(
        null=True, blank=True, verbose_name="Содержание блога", help_text="Введите содержание блога"
    )
    preview = models.ImageField(
        upload_to="blogs/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью блога",
    )
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    is_published = models.BooleanField(
        default=False, verbose_name="Опубликовано", help_text="Отметьте, если блог опубликован"
    )
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров", help_text="Введите количество просмотров"
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.header
