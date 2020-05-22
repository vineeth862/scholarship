from django.shortcuts import render
from .models import post,offline
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils import timezone
import datetime
from django.core.paginator import Paginator

def home_page(request):
    today=datetime.date.today()
    tdelta=datetime.timedelta(days=5)
    add=today+tdelta
   # to get only top 5 post on recent posts
    posts=post.objects.order_by('-posted_on')
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    context={
        "add":add,
        "today":today,
        "posts":posts

    }

    return render(request,'index.html',context)
class PostListView_total(ListView):
    model = post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-posted_on']
    paginate_by = 5

class PostListView_offline(ListView):
    model = offline
    template_name = 'post_list_offline.html'
    context_object_name = 'posts'
    ordering = ['-posted_on']
    paginate_by = 5


class PostListView_scholl(ListView):
    model = post
    template_name = 'post_list_scholl.html'
    context_object_name = 'posts'
    ordering = ['-posted_on'] #to show latest post first add '-'



class PostListView_puc(ListView):
    model = post
    template_name = 'post_list_puc.html'
    context_object_name = 'posts'
    ordering = ['-posted_on'] #to show latest post first add '-'


class PostListView_ug(ListView):
    model = post
    template_name = 'post_list_ug.html'
    context_object_name = 'posts'
    ordering = ['-posted_on'] #to show latest post first add '-'


class PostListView_pg(ListView):
    model = post
    template_name = 'post_list_pg.html'
    ordering = ['-posted_on'] #to show latest post first add '-'
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin,DetailView):
    model=post
    template_name = 'post_detail.html'

class PostDetailView_offline(LoginRequiredMixin,DetailView):
    model=offline
    template_name = 'post_detail_offline.html'

class PostListView_category(ListView):
    model=post
    template_name = 'post_category.html'

class PostListView_minorities(ListView):
    model = post
    template_name = 'post_list_minorities.html'
    ordering = ['-posted_on'] #to show latest post first add '-'
    context_object_name = 'posts'

class PostListView_backward(ListView):
    model = post
    template_name = 'post_list_backward.html'
    ordering = ['-posted_on'] #to show latest post first add '-'
    context_object_name = 'posts'

class PostListView_sc(ListView):
    model = post
    template_name = 'post_list_sc.html'
    ordering = ['-posted_on'] #to show latest post first add '-'
    context_object_name = 'posts'

def test(request):
    return render(request,'')