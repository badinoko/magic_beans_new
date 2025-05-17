from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)  # File ID / URL
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Сидбанк"
        verbose_name_plural = "Сидбанки"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Тип сорта"
        verbose_name_plural = "Типы сортов"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    characteristics = models.TextField(blank=True, null=True)
    photos = models.JSONField(default=list, blank=True)  # список File ID или URL
    hidden = models.BooleanField(default=False)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name="products")
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Сорт"
        verbose_name_plural = "Сорта"
        unique_together = ("name", "producer")

    def __str__(self):
        return self.name


class ProductPackage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="packages")
    title = models.CharField(max_length=50)  # Название фасовки: 3, 3+1, 5 Promo и т.д.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # количество упаковок

    class Meta:
        verbose_name = "Фасовка"
        verbose_name_plural = "Фасовки"

    def __str__(self):
        return f"{self.title} — {self.price} руб. (остаток: {self.stock})"
