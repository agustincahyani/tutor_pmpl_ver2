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
	elif item_counter >= 5 && item_counter < 9:
		the_comment = 'oh tidak'
	else item_counter >= 9
		the_comment = 'Semangat, kerja keras!'
	return render(request, 'home.html', {'comment': the_comment},)

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	item_counter = Item.objects.filter(list=list_).count()
	error = None

	the_comment = ""
	if item_counter == 0:
		the_comment = 'yey, waktunya berlibur'
	elif item_counter < 5:
		the_comment = 'sibuk tapi santai'
	else:
		the_comment = 'oh tidak'

	if request.method == 'POST':
		try:
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			error = "You can't have an empty list item"
	return render(request, 'list.html', {'list': list_, 'comment': the_comment, 'error': error})

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
	return redirect(list_)

def blog_page(request):
	return render(request, 'blog.html',)