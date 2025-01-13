from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name="Продукт 1")

        products = [
            {"name": "Тест1", "description": "Тестовый продукт 1", "category": category, "price": "0.00"},
            {"name": "Тест2", "description": "Тестовый продукт 2", "category": category, "price": "0.01"},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exists: {product.name}"))
