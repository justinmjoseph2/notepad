from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render, redirect

from .models import Note
from .forms import NoteForm

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note:note_list')
    else:
        form = NoteForm()
    return render(request, 'note/add_note.html', {'form': form})

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note/note_list.html', {'notes': notes})


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('note:note_list')
    return redirect('note:note_list') 