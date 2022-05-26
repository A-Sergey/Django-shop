from django.shortcuts import render, get_object_or_404
from .models import Post
#from shop.views import get_AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm

# def post_list(request):
    # posts_list = Post.objects.all()
    # paginator = Paginator(posts_list,3,orphans=1)
    # page = request.GET.get('page')
    # #page_range = paginator.get_elided_page_range(number=page)
    # try:
        # posts = paginator.page(page)
        
    # except PageNotAnInteger:
        # posts= paginator.page(1)
    # except EmptyPage:
        # posts = paginator.page(paginator.num_pages)
    # return render(request, 'news.html',{'posts':posts,
                                        # 'page':page,
                                         # 'form':get_AuthenticationForm(),})

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    paginate_orphans = 1
    template_name = 'news.html'
    
    #def get_template_names(self):
    #    return('news.html')
        
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        context['form']=AuthenticationForm()
        return self.render_to_response(context)