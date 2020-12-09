from django.shortcuts import render
from .models import ContactForm
from .forms import CreateNewForm
# Create your views here.


def form(response):
    if response.method == "POST":
        form = CreateNewForm(response.POST)
        if form.is_valid():
            n = response.POST.get("name")
            p = response.POST.get("phone_number")
            e = response.POST.get("email")
            c = response.POST.get("comments")
            form = ContactForm(name=n, phone_number=p, email=e, comments=c)
            form.save()

    else:
        form = CreateNewForm()

    return render(response, "form/contact.html", {"form": form})
