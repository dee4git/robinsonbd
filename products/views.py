from django.shortcuts import render
from .models import Product, CategoryCertification, CategoryFeatures, CategoryHowToUse


# Create your views here.
def view_all_products(request):
    products = Product.objects.all()
    return render(request, 'view-all-products.html', {
        "products": products
    })


def view_product(request, pk):
    product = Product.objects.get(pk=pk)
    certificates = CategoryCertification.objects.filter(category=product.category)
    features = CategoryFeatures.objects.filter(category=product.category)
    print(features)

    return render(request, 'view-product.html', {
        "product": product,
        "certificates": certificates,
        "features": features,
    })
