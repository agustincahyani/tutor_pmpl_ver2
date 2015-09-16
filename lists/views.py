from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item,Comment

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')

	items = Item.objects.all()
	item_counter = items.count()
	the_comment = ""
	if item_counter == 0:
		the_comment = 'yey, waktunya berlibur'
	elif item_counter < 5:
		the_comment = 'sibuk tapi santai'
	else:
		the_comment = 'oh tidak'

	return render(request, 'home.html', {'items': items, 'comment': the_comment})
