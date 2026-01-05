from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostDetailAPIView(APIView):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.order_by('-created')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

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

class post_list(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 2 
    ordering = '-created'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query)
            )

        return queryset

class postDetailView(DetailView):
    model           = Post
    template_name   = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form        = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
        return self.get(request, *args, **kwargs)
