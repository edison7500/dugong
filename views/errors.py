from django.views.defaults import page_not_found, server_error


def not_found(request):
    return page_not_found(request, template_name='base/error/404.html')

def page_error(request):
    return server_error(request, template_name='base/error/500.html')