from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blogs.models import Blogs


class BlogCreateView(CreateView):
    model = Blogs
    fields = ["header", "content", "preview"]
    success_url = reverse_lazy("blogs:blogs")
    template_name = "blogs/blogs_form.html"


class BlogListView(ListView):
    model = Blogs

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogsDetailView(DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ["header", "content", "preview"]
    success_url = reverse_lazy("blogs:blogs")

    def get_success_url(self):
        return reverse("blogs:blogs_detail", args=[self.kwargs.get("pk")])


class BlogsDeleteView(DeleteView):
    model = Blogs
    success_url = reverse_lazy("blogs:blogs")
