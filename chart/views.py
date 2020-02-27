import json
from django.shortcuts import render
from .models import Product


def products(request):
    queryset = Product.objects.all()
    names = [obj.name for obj in queryset]
    prices = [int(obj.price) for obj in queryset]

    context = {
        'names': json.dumps(names),
        'prices': json.dumps(prices),
    }
    return render(request, 'chart/products.html', context)