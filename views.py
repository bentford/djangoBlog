from django.shortcuts import render_to_response
from benford_name.blog.models import Post, Tag
from django.http import HttpResponse

def posts(request):
    posts = Post.objects.all().order_by('-date_created')[:15]
    return render_to_response('blog_posts.html', {'title':'Posts', 'posts':posts})

def posts_for_year(request, year):
    posts = Post.objects.filter(date_created__year=year).order_by('-date_created')
    return render_to_response('blog_posts.html', {'title':'Posts', 'posts':posts})

def posts_for_year_month(request, year, month):
    posts = Post.objects.filter(date_created__year=year, date_created__month=month).order_by('-date_created')
    return render_to_response('blog_posts.html', {'title':'Posts', 'posts':posts})
    
def posts_for_year_month_slug(request, year, month, slug):
    posts = Post.objects.filter(date_created__year=year, date_created__month=month,slug=slug).order_by('-date_created')
    return render_to_response('blog_posts.html', {'title':'Posts', 'posts':posts})

def tags(request, tag):
    posts = Tag.objects.get(name=tag).post_set.all()
    return render_to_response('blog_posts.html', {'title':'Posts', 'posts':posts})

def archive(request):
    posts = Post.objects.all()
    years = [p.date_created.year for p in posts]
    years = set(years) #eliminate duplicates
    return render_to_response('blog_archive.html', {'title':'Archive', 'years':years})