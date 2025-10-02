from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.order_by('-published_date')[:10]
    return render(request, 'blog/index.html', {'posts': posts})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('blog:index')  # adjust to your homepage name
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        # update basic user fields (email) and profile fields
        email = request.POST.get('email', user.email)
        user.email = email
        user.save()

        # If Profile exists and you added ProfileForm:
        if hasattr(user, 'profile'):
            pform = ProfileForm(request.POST, request.FILES, instance=user.profile)
            if pform.is_valid():
                pform.save()
                messages.success(request, "Profile updated.")
                return redirect('blog:profile')
        else:
            messages.success(request, "Profile updated.")
            return redirect('blog:profile')
    else:
        pform = ProfileForm(instance=getattr(user, 'profile', None))
    return render(request, 'blog/profile.html', {'user': user, 'pform': pform})


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# List all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ['-created_at']

# View single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

# Create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm

# If you already have PostDetailView defined, replace it with this or merge its logic.
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comments'] = self.object.comments.all()
        ctx['comment_form'] = CommentForm()
        return ctx

    # handle comment POST from the same URL
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('blog:login')
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect('blog:post-detail', pk=self.object.pk)
        # if invalid, re-render with errors
        ctx = self.get_context_data()
        ctx['comment_form'] = form
        return self.render_to_response(ctx)

# Edit comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        # ensure author remains the same
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

# Delete comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']  # Only ask user for comment text
    template_name = 'blog/add_comment.html'

    # Automatically set the author and post
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)

    # Redirect back to the post detail page after saving
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.kwargs['post_id']})



from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from taggit.models import Tag
from .models import Post

def search_posts(request):
    q = request.GET.get('q', '').strip()
    results = []
    if q:
        # Search title or content
        results = Post.objects.filter(
            Q(title__icontains=q) | Q(content__icontains=q) | Q(tags__name__icontains=q)
        ).distinct()
    return render(request, 'posts/search_results.html', {'query': q, 'results': results})

def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__slug__in=[tag_slug]).distinct()
    return render(request, 'posts/posts_by_tag.html', {'tag': tag, 'posts': posts})
