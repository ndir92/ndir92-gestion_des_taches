
from .models import Task
from .forms import TacheForm
from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.

def index(request):
    form = TacheForm(request.POST or None)
    if form.is_valid():
        form.save()
    content = Task.objects.all()
    return render(request, 'index.html', {'taches':content, 'form':form})


def update(request, my_id):
    obj = get_object_or_404(Task, id=my_id)
    form = TacheForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form })




def delete(request, my_id):
    obj = get_object_or_404(Task, id=my_id)
    obj.delete()
    return redirect('/')              
     
