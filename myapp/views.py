from django.shortcuts import render, redirect
from .models import About, Project, Contact
from .forms import FormContact
# Create your views here.
def index(request):
    about = About.objects.get(id=1)
    projects = Project.objects.all()


    context = {
        'about': about,
        'projects': projects,
        'form': FormContact()
    }
    return render(request, 'index.html', context)

def send_contact(request):
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/#contact')
        return redirect('/#contact')
    return render(request, 'index.html')
