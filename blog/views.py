from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #blog/post_list.html意味着要创建post_list.html模板
    #{'posts': posts}意味着'posts'中的posts这个名字可以在html意味着要创建post_list.html模板中使用
    return render(request, 'blog/post_list.html', {'posts': posts})

#pk是在urls.py中设置的参数
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})






