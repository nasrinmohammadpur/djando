
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Post
#from .forms import ImageForm

def post_list(request):
    posts_all = Post.objects.filter(status='published')
    return render(request,
    'products/post/list.html',
    {'posts': posts_all})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day)   
    return render(request,
    'products/post/detail.html',
    {'post': post})

#def products(request):
       # infos = post_detail.objects.all()
       # if request.method == 'POST':
       #     form = ImageForm(request.POST, request.FILES)
       #     if form.is_valid():
       #        Post(name=form.cleaned_data['name'], image=request.FILES['image']).save()
       #        return redirect('home:home')
       # else:
        #    form = ImageForm()
      #  return render(request, 'products/post/detail.html', {'form':form, 'infos':infos})
            
