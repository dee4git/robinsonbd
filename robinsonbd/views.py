from django.shortcuts import render
from products.models import Category


def home(request):
    """shows the home content"""

    categories = Category.objects.all()
    return render(request, 'index.html', {
        "categories": categories,
    })
