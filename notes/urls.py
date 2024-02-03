from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotePageView.as_view(), name="notes.item"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.edit"),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    path('notes/new', views.CreateNotesView.as_view(), name="notes.new"),
]