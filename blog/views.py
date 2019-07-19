from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.utils import timezone
from .models import Post
from datetime import datetime

'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts})
'''

'''def a_view(request):
    return render_to_response("post_list.html", {
        'time':datetime.now(),
        }, context_instance=RequestContext(request))
'''
def a_view(request):
    return render(request, 'blog/post_list.html',{'time':datetime.now()})
>>>>>>> f116712c0aaa338db2c5dd00fb2f98930e6daa24
