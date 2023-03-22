from django.shortcuts import render
from .models import Product, CategoryCertification, CategoryFeatures, CategoryHowToUse


# Create your views here.
def view_all_products(request):
    products = Product.objects.order_by('serial_number').filter(upcoming=False)
    upcoming_products = Product.objects.order_by('serial_number').filter(upcoming=True)
    return render(request, 'view-all-products.html', {
        "products": products,
        "upcoming_products": upcoming_products,
    })


def view_product(request, pk):
    product = Product.objects.get(pk=pk)
    certificates = CategoryCertification.objects.filter(category=product.category)
    features = CategoryFeatures.objects.filter(category=product.category)
    how_to_use = CategoryHowToUse.objects.filter(category=product.category)

    return render(request, 'view-product.html', {
        "product": product,
        "certificates": certificates,
        "features": features,
        "how_to_use": how_to_use,
    })
