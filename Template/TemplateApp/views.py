from django.shortcuts import render


def desplegarTemplate(request):
    data = {"nombre" : "Paul"}
    return render(request, 'tenplateapp/ejemplo1.html', data)
