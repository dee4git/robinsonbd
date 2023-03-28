from django.shortcuts import render

from extras.models import Stuff, Application, Service, QnA
from products.models import Category, CategoryFeatures, CategoryCertification, Banner


def home(request):
    """shows the home content"""
    category_information = []  # keeps all the category information in a list of list
    categories = Category.objects.all()
    applications = Application.objects.all()
    services = Service.objects.all()
    faqs = QnA.objects.all()
    stuffs = Stuff.objects.order_by('serial_number')
    banners = Banner.objects.order_by('serial_number')

    # making a pair of all the information related to a category
    for category in categories:
        features = CategoryFeatures.objects.filter(category=category)
        certificates = CategoryCertification.objects.filter(category=category)
        category_information.append([category, features, certificates])
    return render(request, 'index.html', {
        "category_information": category_information,
        "stuffs": stuffs,
        "applications": applications,
        "services": services,
        "faqs": faqs,
        "banners": banners,
    })
