from django.shortcuts import render


def not_found(request):
    return render(request, status=404, template_name='base/errors/404.html')


def page_error(request):
    return render(request, status=500, template_name='base/errors/500.html')
