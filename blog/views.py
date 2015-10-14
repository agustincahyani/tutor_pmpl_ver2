from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

def blog_page(request):
	return render(request, 'blog.html',)
