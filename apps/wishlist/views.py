from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from .models import Item

def current_user(request):
    return User.objects.get(id=request.session['user_id'])


def flash_errors(request, errors):
    for error in errors:
        messages.error(request, error)

def user(request, id):
    context={
        'user' : current_user(request),
    }
    return render(request, 'wishlist/items.html', context)

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user = current_user(request)
    context = {
        'user': user, 
        'notwished': Item.objects.exclude(wished_by = user),
    }
    return render(request, 'wishlist/index.html', context)

def show_item(request, item_id):
    item = Item.objects.get(id = item_id)
    context = {
        'item': item,
        'users': item.wished_by.all()
    }
    return render(request, 'wishlist/items.html', context)

def create(request):
    if request.method == "POST":
        errors = Item.objects.validate(request.POST)

        if not errors:
            item = Item.objects.create_item(request.POST, request.session["user_id"])
            return redirect(reverse('add_wish', args = (item.id, )))

        flash_errors(request, errors)
        return redirect(reverse('create_item'))
    else:
        return render(request, 'wishlist/create.html')

def add_wish(request,item_id):
    Item.objects.add_wish(item_id, request.session["user_id"])
    return redirect(reverse('dashboard'))


def remove_wish(request,item_id):
    Item.objects.remove_wish(item_id, request.session["user_id"])
    return redirect(reverse('dashboard'))


def delete(request, item_id):
    Item.objects.delete_item(item_id)
    return redirect(reverse('dashboard'))