from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
	items = Item.objects.all()
	item_counter = items.count()
	the_comment = ""
	if item_counter == 0:
		the_comment = 'yey, waktunya berlibur'
	elif item_counter < 5:
		the_comment = 'sibuk tapi santai'
	else:
		the_comment = 'oh tidak'

	return render(request, 'home.html', {'comment': the_comment},)

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items},)

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/the-only-list-in-the-world/')
