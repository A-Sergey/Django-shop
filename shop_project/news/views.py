from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 7
    paginate_orphans = 1
    template_name = "news.html"
