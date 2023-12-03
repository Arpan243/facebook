from django.shortcuts import render
import shortuuid
from core.models import Post
from django.http import JsonResponse
from django.utils.timesince import timesince
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    posts = Post.objects.filter(active=True, visibility="Everyone")
    context = {"posts": posts}
    return render(request, "core/index.html", context)

@csrf_exempt
def create_post(request):

    if request.method == 'POST':
        title = request.POST.get('post-caption')
        visibility = request.POST.get('visibility')
        image = request.FILES.get('post-thumbnail')

        print("Title ============", title)
        print("thumbnail ============", image)
        print("visibility ============", visibility)

        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:4]

        if title and image:
            post = Post(title=title, image=image, visibility=visibility, user=request.user, slug=slugify(title) + "-" + str(uniqueid.lower()))
            post.save()

            
            return JsonResponse({'post': {
                'title': post.title,
                'image_url': post.image.url,
                "full_name":post.user.profile.full_name,
                "profile_image":post.user.profile.image.url,
                "date":timesince(post.date),
                "id":post.id,
            }})
        else:
            return JsonResponse({'error': 'Invalid post data'})

    return JsonResponse({"data":"Sent"})

@csrf_exempt
def like_post(request):

    id = request.GET['id']
    post = Post.objects.get(id=id)
    user = request.user
    bool = False 

    if user in post.likes.all():
        post.likes.remove(user)
        bool = False
    else:
        post.likes.add(user)
        bool = True 
        # Do this during noticiation lecture
        if post.user != request.user:
            send_notification(post.user, user, post, None, noti_new_like)

    data = {
        "bool":bool,
        'likes':post.likes.all().count()
    }
    return JsonResponse({"data":data})
