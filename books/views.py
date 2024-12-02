from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import AuthorForm

# Create your views here.

def book_list(request):
  books = Book.objects.all()
  return render(request, 'books/book_list.html', { 'books': books })

def book_create(request):
  if request.method == 'POST':
    title = request.POST['title']
    author_id = request.POST['author']
    description = request.POST['description']
    published_date = request.POST['published_date']
    
    author = Author.objects.get(id=author_id)
    
    Book.objects.create(
      title=title,
      author=author,
      description=description,
      published_date=published_date
    )
    return redirect('book_list')
  
  authors = Author.objects.all()
  return render(request, 'books/book_form.html', { 'authors': authors})


def book_detail(request, id):
  book = get_object_or_404(Book, id=id)
  return render(request, 'books/book_detail.html', {'book': book})

def book_update(request, id):
  book = get_object_or_404(Book, id=id)
  if request.method == 'POST':
    book.title = request.POST['title']
    author_id = request.POST['author']
    book.author = Author.objects.get(id=author_id)
    book.description = request.POST['description']
    book.published_date = request.POST['published_date']
    book.save()
    return redirect('book_list')
  
  authors = Author.objects.all()
  return render(request, 'books/book_form.html', {'book': book,  'authors': authors})

def book_delete(request, id):
  book = get_object_or_404(Book, id=id)
  if request.method == 'POST':
    book.delete()
    return redirect('book_list')
  return render(request, 'books/book_confirm_delete.html', {'book': book})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # Redirect to author list after saving
    else:
        form = AuthorForm()
    return render(request, 'books/author_form.html', {'form': form})
  
def author_list(request):
  authors = Author.objects.all()
  return render(request, 'books/author_list.html', {'authors': authors})
