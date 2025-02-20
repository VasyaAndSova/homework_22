from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def form_valid(self, form):
        return super().form_valid(form)


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")
