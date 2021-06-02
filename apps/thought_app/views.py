from django.shortcuts import render, redirect
from ..logreg_app.models import User
from . models import Thought
from django.db.models import Count
from django.contrib import messages
# Create your views here.
def dashboard(request):
    try:
        user_selected = User.objects.get(id = int(request.session['userid']))
        thoughts = Thought.objects.all()
        thoughts_ordered = Thought.objects.annotate(count = Count('likes')).order_by('-count')
        context = {
            'thoughts': thoughts_ordered,
            'user_selected': user_selected
        }
        return render(request, 'thought_dashboard.html', context)
    except:
        return redirect('/')

def add(request):
    try:
        user_selected = User.objects.get(id = int(request.session['userid']))
        errors = Thought.objects.thought_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Thought.objects.create(
                owner = user_selected,
                thought = request.POST['thought']
            )
        return redirect('/thoughts')
    except:
        return redirect('/')

def thought_detail(request, thought_id):
    try:
        user_selected = User.objects.get(id = int(request.session['userid']))
        thought = Thought.objects.get(id = int(thought_id))
        thought_owner = thought.owner.id
        thought_likes = thought.likes.all()
        thought_exclude = thought_likes.exclude(id = thought_owner)
        context = {
            'thought': thought,
            'user_selected': user_selected,
            'thought_exclude': thought_exclude
        }
        return render(request, 'thought.html', context)
    except:
        return redirect('/')

def delete(request, thought_id):
    thought = Thought.objects.get(id = int(thought_id))
    thought.delete()
    return redirect('/thoughts')

def like(request, thought_id):
    thought = Thought.objects.get(id = int(thought_id))
    user_selected = User.objects.get(id = int(request.session['userid']))
    thought.likes.add(user_selected)
    return redirect(f'/thoughts/{thought_id}')

def unlike(request, thought_id):
    thought = Thought.objects.get(id = int(thought_id))
    user_selected = User.objects.get(id = int(request.session['userid']))
    thought.likes.remove(user_selected)
    return redirect(f'/thoughts/{thought_id}')