from django.shortcuts import render


def home(request):
    context = {
        'user': request.user
    }
    return render(request, 'base.html', context)
