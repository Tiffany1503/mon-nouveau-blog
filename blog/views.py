from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Airlines
from .forms import PostForm

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def airline_ranking(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/airline_ranking.html', {'airlines': airlines})

def ranking_by_country(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/ranking_by_country.html', {'airlines': airlines})

def be(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/be.html', {'airlines': airlines})

def br(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/br.html', {'airlines': airlines})

def ca(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/ca.html', {'airlines': airlines})

def da(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/da.html', {'airlines': airlines})

def fr(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/fr.html', {'airlines': airlines})

def al(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/al.html', {'airlines': airlines})

def gr(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/gr.html', {'airlines': airlines})

def ir(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/ir.html', {'airlines': airlines})

def it(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/it.html', {'airlines': airlines})

def ja(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/ja.html', {'airlines': airlines})

def me(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/me.html', {'airlines': airlines})

def pb(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/pb.html', {'airlines': airlines})

def no(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/no.html', {'airlines': airlines})

def pol(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/pol.html', {'airlines': airlines})

def por(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/por.html', {'airlines': airlines})

def es(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/es.html', {'airlines': airlines})

def su(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/su.html', {'airlines': airlines})

def tu(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/tu.html', {'airlines': airlines})

def eau(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/eau.html', {'airlines': airlines})

def uk(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/uk.html', {'airlines': airlines})

def usa(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/usa.html', {'airlines': airlines})

def airline(request):
    airlines = Airlines.objects.all()
    return render(request, 'blog/airline.html', {'airlines': airlines})