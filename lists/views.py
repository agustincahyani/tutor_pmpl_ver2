from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
	item_counter = 0
	the_comment = ""
	if item_counter == 0:
		the_comment = 'yey, waktunya berlibur'
	elif item_counter < 5:
		the_comment = 'sibuk tapi santai'
	else:
		the_comment = 'oh tidak'
	return render(request, 'home.html', {'comment': the_comment},)

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	item_counter = Item.objects.filter(list=list_).count()

	the_comment = ""
	if item_counter == 0:
		the_comment = 'yey, waktunya berlibur'
	elif item_counter < 5:
		the_comment = 'sibuk tapi santai'
	else:
		the_comment = 'oh tidak'

	return render(request, 'list.html', {'list': list_, 'comment': the_comment})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	text_ = request.POST['item_text']
	if text_ == "":
		return render(request, 'list.html', {'list': list_, 'error_message': "You can't have an empty list item"})
	else:
		Item.objects.create(text=text_, list=list_)
		return redirect('/lists/%d/' % (list_.id,))

def blog_page(request):
	return render(request, 'blog.html',)