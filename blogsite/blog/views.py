from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required ##function-based view
from django.contrib.auth.mixins import (
    LoginRequiredMixin, ##class-based view
    UserPassesTestMixin #so that only author can update post
)
from django.contrib.auth.models import User




#Create your views here.
# posts = [
#     {
#         'author': 'SecretAgent',
#         'title': 'Blog Post 1',
#         'content': 'my post content',
#         'date_posted': 'April 27, 2022'
#     },
#     {
#         'author': 'SecretAgent',
#         'title': 'Blog Post 2',
#         'content': 'new post content',
#         'date_posted': 'April 28, 2022'
#     }
# ]

@login_required
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


    # posts = list(Post.objects.values())
    # return JsonResponse(posts,safe=False)


class PostListView(ListView):
    model= Post
    template_name = 'blog/home.html' #blog/post_list.html
    context_object_name = 'posts'
    ordering = '-date_posted'
    # paginate_by = 6

class PostDetailView(DetailView): #blog/post_detail.html
    model= Post

class PostCreateView(LoginRequiredMixin,CreateView): #blog/post_form.html
    model= Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): #blog/post_form.html
    model= Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): #blog/post_confirm_delete.html
    model= Post
    
    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False


class UserPostListView(ListView):
    model= Post
    template_name = 'blog/home.html' #blog/post_list.html
    context_object_name = 'posts'
    ordering = '-date_posted'
    # paginate_by = 6 

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(author=user)



@login_required
def about(request):
    return render(request, 'blog/about.html')