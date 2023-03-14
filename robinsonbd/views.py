from django.shortcuts import render
from products.models import Category, CategoryFeatures, CategoryCertification


def home(request):
    """shows the home content"""
    category_information = []  # keeps all the category information in a list of list
    categories = Category.objects.all()
    # making a pair of all the information related to a category
    for category in categories:
        features = CategoryFeatures.objects.filter(category=category)
        certificates = CategoryCertification.objects.filter(category=category)
        category_information.append([category, features, certificates])
    return render(request, 'index.html', {
        "category_information": category_information,
    })
