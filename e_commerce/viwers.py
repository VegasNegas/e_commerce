from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    context = {
        "title": "Pagina Principal",
        "content": "Pagina Inicial"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Pagina Sobre",
        "content": "Pagina Sobre"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    context = {
        "title": "Pagina de contato",
        "content": "Pagina de contato"
    }
    return render(request, "contact/view.html", context)