from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование категории", help_text="Введите наименование категории"
    )
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование продукта", help_text="Введите наименование продукта"
    )
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображние",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию продукта",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена", help_text="Введите цену за покупку"
    )
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "price"]

    def __str__(self):
        return self.name
