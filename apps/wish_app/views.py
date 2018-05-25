from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Wish
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'my_wish': Wish.objects.filter(wisher=request.session['user_id']),
        'not_wish' : Wish.objects.exclude(wisher=request.session['user_id'])
    }
    return render(request, 'wish_app/dash.html', context)
def add(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'wish_app/add.html')
def createWish(request):
    if 'user_id' not in request.session:
        return redirect('/')
    result = Wish.objects.createWish(request.POST, request.session['user_id'])
    if result['status'] == False:
        for error in result['errors']:
            messages.error(request, error)
            return redirect('/wish/add')
    return redirect('/wish')
def delete(request, wish_id):
    if 'user_id' not in request.session:
        return redirect('/')
    delete_wish = Wish.objects.get(id=wish_id)
    delete_wish.delete()
    return redirect('/wish')
def remove(request, wish_id):
    if 'user_id' not in request.session:
        return redirect('/')
    remove_wish = Wish.objects.removewishlist(wish_id=wish_id, user_id=request.session['user_id'])
    return redirect('/wish')
def joinWishlist(request, wish_id):
    if 'user_id' not in request.session:
        return redirect('/')
    Wish.objects.joinWishlist(wish_id=wish_id, user_id=request.session['user_id'])
    return redirect('/wish')
def wish_item(request, wish_id):
    if 'user_id' not in request.session:
        return redirect('/')
    wish = Wish.objects.get(id=wish_id)
    context = {
        'item' : wish,
        'wishers' : wish.wisher.all()
    }
    return render(request, 'wish_app/wish.html', context)
