from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product

class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"