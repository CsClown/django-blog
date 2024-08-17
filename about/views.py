from django.shortcuts import render, Http404
from .models import About

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

    if about is None:
        raise Http404('About Me page not found')

    return render(
        request,
        "about/about.html",
        {"about": about},

    )