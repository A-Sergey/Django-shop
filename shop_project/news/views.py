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
    paginate_by = 3
    paginate_orphans = 1
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
        try:
            product_of_the_day = Product.objects.get(product_of_the_day=True)
        except:
            product_of_the_day = None
        context['product_of_the_day']=product_of_the_day
        context['products_sale']=products_sale
        context['form']=AuthenticationForm()
        return context