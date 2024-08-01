from django.core.management.base import BaseCommand
from .models import Category, Product
import json

class Command(BaseCommand):
    help = 'Импорт категорий и продуктов из JSON-файла'

    def handle(self, *args, **options):
        # Удаление всех продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Чтение данных из JSON-файла
        with open('data.json', 'r') as file:
            data = json.load(file)

        # Создание категорий
        categories = []
        for category_data in data['categories']:
            category = Category(
                name=category_data['name'],
                description=category_data['description']
            )
            categories.append(category)
        Category.objects.bulk_create(categories)

        # Создание продуктов
        products = []
        for product_data in data['products']:
            category = Category.objects.get(pk=product_data['category'])
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                image=product_data['image'],
                category=category,
                price=product_data['price']
            )
            products.append(product)
        Product.objects.bulk_create(products)

        self.stdout.write(self.style.SUCCESS('Категории и продукты успешно импортированы из JSON-файла'))