from django.shortcuts import render
from .forms import ContactForm

def home(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = ContactForm()

    return render(request, 'main/index.html', {
        'form': form
    })
