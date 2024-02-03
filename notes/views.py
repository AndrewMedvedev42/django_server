from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NotesForm
from .models import Notes
# Create your views here.

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = "/notes"
    template_name = "notes/notes_delete.html"

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = "/notes"
    form_class = NotesForm
    template_name = "notes/note_form.html"

class CreateNotesView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = "/notes"
    form_class = NotesForm
    template_name = "notes/note_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotePageView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/note_item.html" 

