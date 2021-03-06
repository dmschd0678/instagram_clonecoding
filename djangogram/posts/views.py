from django.shortcuts import get_object_or_404, render
from djangogram.users.models import User as user_model

from . import models

# Create your views here.
def index(request):
    return render(request, 'posts/base.html')

def post_create(request):
    if request.method == "GET":
        return render(request, 'posts/post_create.html')
    elif request.method == "POST":
        # 로그인이 되어 있을 때
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, pk=request.user.id)
            
            image = request.FILES['image']
            caption = request.POST['caption']
            
            new_post = models.Post.objects.create(
                author = user,
                image = image,
                caption = caption
            )
            new_post.save()
            
            return render(request, 'post/base.html')
        else:
            return render(request, 'users/main.html')