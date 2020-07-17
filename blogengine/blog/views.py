from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TagForm, PostForm
from django.core.paginator import Paginator
from .models import *
from django.views.generic import View
from .utils import *
from django.db.models import Q


def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query), Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'blog/index.html', context=context)


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/post_tags.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


def post_redirect(request):
    return HttpResponseRedirect('/blog/')


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class TagEdit(LoginRequiredMixin, ObjectEditMixin, View):
    model = Tag
    form = TagForm
    template = 'blog/tag_edit.html'
    raise_exception = True


class PostEdit(LoginRequiredMixin, ObjectEditMixin, View):
    model = Post
    form = PostForm
    template = 'blog/post_edit.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    url = 'tags_lists'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    url = 'posts_list'
    raise_exception = True
