from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html',{'form': form} )
@login_required
def post_create(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

# def post_list(request):
#     post_list       = Post.objects.order_by('-created')
#     paginator       = Paginator(post_list,2)
#     page_number     = request.GET.get('page')
#     page_obj        = paginator.get_page(page_number)

#     return render(request, 'blog/post_list.html', {'page_obj':page_obj})

class post_list(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 2 
    ordering = '-created'


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render (request, 'blog/post_detail.html', {'post':post})
