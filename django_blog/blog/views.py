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
