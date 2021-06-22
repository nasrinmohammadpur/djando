
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Post
#from .forms import ImageForm
from .forms import EmailPostForm
from django.core.mail import send_mail

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


def post_share(request, post_id):
     # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
            # Form was submitted
            form = EmailPostForm(request.POST)
            if form.is_valid():
                # Form fields passed validation
                cd = form.cleaned_data
                # ... send email
                post_url = request.build_absolute_uri(
                    post.get_absolute_url())
                subject = f"{cd['name']} recommends you read " \
                          f"{post.title}"
                message = f"Read {post.title} at {post_url}\n\n" \
                          f"{cd['name']}\'s comments: {cd['comments']}"
                send_mail(subject, message, 'admin@myproducts.com',
                          [cd['to']])
                sent = True
    else:
            form = EmailPostForm()
    return render(request, 'products/post/share.html', {'post': post,
                                                        'form': form,
                                                        'sent': sent})


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
            
