from django.shortcuts import render
from . import models


def index(request):
    context = {
        'num_books': models.Book.objects.count(),
        'num_instances': models.BookInstance.objects.count(),
        'num_available': models.BookInstance.objects.filter(status=0).count(),
        'num_authors': models.Author.objects.count(),
        'genres': models.Genre.objects.all(),
    }
    return render(request, 'library/index.html', context)
