from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Blog

# Create your views here.
def home(request):
    posts = Blog.objects.all()
    return render(request, 'index.html', {'posts' : posts})


def contact(request):
    return render(request, 'contact.html')

def createpage(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        #Blog.objects.create(title=title, content=content)
        postmade = Blog(title=title, content=content)
        if postmade is not None:
            postmade.save()
            return redirect('home')  
    return render(request, 'createpage.html')

def delete(request, id):
    post = Blog.objects.get(id=id)
    post.delete()
    return redirect(request, 'home')
    