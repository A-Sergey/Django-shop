from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm
from products.models import Product
from django.db.models import Q


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 7
    paginate_orphans = 1
    template_name = 'news.html'