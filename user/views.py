from django.shortcuts import render


def index(request):
    context = {
        'title': 'Dashboard',
        'side_bar_urls': get_urls(),
    }
    return render(request, 'pages/dashboard.html',context=context)


def get_urls():
    return {
        'index': {
            'url': '/user/index/',
            'icon': 'fa fa-dashboard',
            'title': 'Dashboard',
        },
    }
