from .models import Service, Application


def get_services(request):
    return {"all_services": Service.objects.all()}


def get_applications(request):
    return {"all_applications": Application.objects.all()}
