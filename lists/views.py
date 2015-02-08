from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	# 	new_item_text = request.POST['item_text']
	# 	Item.objects.create(text=new_item_text)
	# else:
	# 	new_item_text = ''
	# item = Item()
	# item.text = request.POST.get('item_text', '')
	# item.save()
	# items = Item.objects.all()
	return render(request, 'lists/home.html')
	# return render(request, 'lists/home.html', {
	# 	'new_item_text': new_item_text
	# 	})

def view_list(request):
	items = Item.objects.all()
	return render(request, 'lists/list.html', {'items': items})