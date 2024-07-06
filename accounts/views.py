from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            elif user.user_type == 'doctor':
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def doctor_dashboard(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('doctor_dashboard')  # Redirect to the same page after form submission
    else:
        form = BlogPostForm()
    
    # Retrieve blogs authored by the current doctor
    blogs = BlogPost.objects.filter(author=request.user)
    
    context = {
        'form': form,
        'blogs': blogs,
    }
    return render(request, 'doctor_dashboard.html', context)

def patient_dashboard(request):
    # Retrieve published blogs (not drafts)
    blogs = BlogPost.objects.filter(draft=False)
    
    context = {
        'blogs': blogs,
    }
    return render(request, 'patient_dashboard.html', context)

def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'blog_post': blog_post})