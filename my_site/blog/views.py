from django.shortcuts import render, get_object_or_404
from.models import Post


# Create your views here.

all_posts = [

    

]


#helper function
def get_date(post):
    return post['date']


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{

        "posts" : latest_posts
    })

def posts(request):
    all_posts = get_object_or_404(Post)
    return render(request,"blog/all-post.html",{
        "all_posts":all_posts
    })

def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    return render(request,"blog/post-detail.html",{
        "post": identified_post
    })