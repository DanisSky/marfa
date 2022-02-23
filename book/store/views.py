# Create your views here.
from django.views.generic import ListView, TemplateView

from store.models import Service, Book


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = ''

    def get_queryset(self):
        return Service.objects.all()


class ProductListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = ''

    def get_queryset(self):
        return Book.objects.all()


class IndexView(TemplateView):
    template_name = 'index.html'
