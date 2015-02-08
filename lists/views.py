from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Item, List

def home_page(request):
	return render(request, 'lists/home.html')
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['item_text'])
	# 	return redirect('/lists/the-only-list-in-the-world/')
	# 	new_item_text = request.POST['item_text']
	# 	Item.objects.create(text=new_item_text)
	# else:
	# 	new_item_text = ''
	# item = Item()
	# item.text = request.POST.get('item_text', '')
	# item.save()
	# items = Item.objects.all()
	# return render(request, 'lists/home.html')
	# return render(request, 'lists/home.html', {
	# 	'new_item_text': new_item_text
	# 	})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	# items = Item.objects.filter(list=list_)
	# items = Item.objects.all()
	# return render(request, 'lists/list.html', {'items': items})
	return render(request, 'lists/list.html', {'list': list_})






