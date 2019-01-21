from django.shortcuts import render

from django.http import HttpResponse
from .models import Post
from .forms import postForm
from .forms import commentform

# Create your views here.
def index(request):
    context = {}
    post = Post.objects.all()
    context['post'] = post
    return render(request, 'index.html', context)


def help(request):
    return HttpResponse('Sample!')

def detail(request, question_id):
    context = {}
    context['post'] = Post.objects.get(id=question_id)
    return render(request, 'detail.html' , context)



def update(request,question_id):
    if request.method == 'POST':
        pass
    else:
            question = Post.objects.get(id=question_id)
            context = {}
            context['form'] = postForm(instance=question)
            context['q_id'] = question_id
            return render(request, 'update.html', context)
