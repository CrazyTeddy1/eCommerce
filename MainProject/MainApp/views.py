from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {"title": "Welcome to the page",
                "content": "This is my content",

    }
    if request.user.is_authenticated:
        context["premium_content"] = "You are now a premium viewer"
    return render(request, 'MainApp/home_page.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {"title": "Contact page",
                "content": "This is my content",
                "form": contact_form,
                "premium_content": "Welcome to my shop"

    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    #if request.method == 'POST':
        #pass
    return render(request, 'MainApp/contact_page.html', context)


def about_page(request):
    context = {"title": "About Page",
                "content": "This is my content"

    }
    return render(request, 'MainApp/home_page.html', context)





def login_page(request):

    form = LoginForm(request.POST or None)
    context = {

        "form":form
    }


    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/")
        else:
            print('Error')

    return render(request, "MainApp/login.html", context)





User = get_user_model()
def register_page(request):

    form = RegisterForm(request.POST or None)
    context = {

        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        new_user = User.objects.create_user(username, email, password)
        new_user.save()

        


    return render(request, 'MainApp/register.html', context)
