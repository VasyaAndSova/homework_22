from django.urls import path

from blogs.views import BlogCreateView, BlogListView, BlogsDeleteView, BlogsDetailView, BlogsUpdateView

app_name = "blogs"

urlpatterns = [
    path("blogs/", BlogListView.as_view(), name="blogs"),
    path("blogs/detail/<int:pk>/", BlogsDetailView.as_view(), name="blogs_detail"),
    path("blogs/update/<int:pk>/", BlogsUpdateView.as_view(), name="blogs_update"),
    path("blogs/create/", BlogCreateView.as_view(), name="blogs_create"),
    path("blogs/delete/<int:pk>/", BlogsDeleteView.as_view(), name="blogs_delete"),
]
