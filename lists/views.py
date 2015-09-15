from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item,Comment

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		the_item = request.POST.get('item_text', '')
		the_comment = request.POST.get('comment_text', '')
		if the_item:
			Item.objects.create(text=the_item)

		if the_comment:
			Comment.objects.create(text=the_comment)

		return redirect('/')

	items = Item.objects.all()
	comments = Comment.objects.all()
	return render(request, 'home.html', {'items': items, 'comments': comments})
