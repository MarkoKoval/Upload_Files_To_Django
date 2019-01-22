from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Document
from .forms import DocumentForm


def list(request):
    # Handle file upload
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = DocumentForm(request.POST, request.FILES)
        print(1)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            print(2)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form
        print(3)
    print(4)
    #Document.objects.all().delete()

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render(request, 'list.html', {'documents': documents, 'form': form})