from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='catalog/photo', null=True, blank=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения", editable=False)
    views_counter = models.PositiveBigIntegerField(verbose_name='Счётчик просмотров', help_text='Укажите количество просмотров', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='parent', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Продукт")
    version_number = models.PositiveBigIntegerField(verbose_name='номер версии', default=1)
    name = models.CharField(max_length=255, verbose_name="Название Версии")
    indicates_the_current_version = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='parent_products', verbose_name="Признаки Текущей Версии", blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Version parent"
        verbose_name_plural = "Version"
        ordering = ['indicates_the_current_version', 'name']


