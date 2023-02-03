from django.shortcuts import render


def index(request):
    context = {
        'title': 'Dashboard',
        'side_bar_urls': get_urls(),
    }
    return render(request, 'pages/dashboard.html',context=context)


def word(request):
    context = {
        'title': 'Word',
        'side_bar_urls': get_urls(),
    }
    return render(request, 'pages/word.html', context=context)


def get_urls():
    return {
        'index': {
            'url': '/user/index/',
            'icon': 'icons/dashboard/side_bar/dashboard-gray.svg',
            'active_icon': 'icons/dashboard/side_bar/dashboard-white.svg',
            'title': 'Dashboard',
        },
        'word': {
            'url': '/user/word/',
            'icon': 'icons/dashboard/side_bar/book-gray.svg',
            'active_icon': 'icons/dashboard/side_bar/book-white.svg',
            'title': 'Word',
        },
    }
