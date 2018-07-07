from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q
from .register_froms import Registration
from django.contrib.auth.forms import UserCreationForm


def login_user(request):

    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect("register")

        return redirect("detail")

    if request.method == "GET":
        form = Registration()
        return render(request, "register_form.html", {'form': form})


def create_post(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "create.html", context)


def delete_post(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("detail")


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "create.html", context)


def stat(request):
    context = {
        "name": "post running",

    }
    return render(request, "index.html", context)


def post_detail(request, id=None):

    # obj = Post.objects.all()

    obj = get_object_or_404(Post, id=id)
    if not request.user.is_staff or not request.user.is_superuser:
        if obj.draft:
            raise Http404
    context = {
        "name": "update running",
        "object_list": obj,
    }
    return render(request, "list.html", context)


def post_list(request):



    obj = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(obj, 4)
    page = request.GET.get("page")

    seek = request.GET.get("find")

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    if seek:
        queryset = Post.objects.filter(Q(title__contains=seek) |
                                       Q(contents__contains=seek)

                                       )

    context = {
        "name": "update running",
        "object_list": queryset,

    }
    return render(request, "index.html", context)



