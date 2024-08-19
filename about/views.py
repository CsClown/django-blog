from django.shortcuts import render, Http404
from .models import About
from django.contrib import messages
from .forms import CollaborateForm

# Create your views here.
def about_view(request):
    """
    Display an individual :model: `about.AboutMe`.

    **Context**

    ``about```
        An instance of :model:`about.AboutMe`.
    
    **Template**

    :template:`about/about.html``
    """

    about = About.objects.first()
    collaborate_form = CollaborateForm()

    if about is None:
        raise Http404('About Me page not found')

    if request.method == "POST":
        print("received a POST request")
        collaborate_form = CollaborateForm(data = request.POST)
        if collaborate_form.is_valid():
            collaboration_request = collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )
            


    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form" : collaborate_form
        },

    )