from django.shortcuts import render

# Create your views here.
from extras.models import Service, Application


def view_service(request, pk):
    service = Service.objects.get(pk=pk)

    return render(request, 'view-service.html', {
        "service": service,

    })


def view_application(request, pk):
    service = Application.objects.get(pk=pk)

    return render(request, 'view-service.html', {
        "service": service,

    })
