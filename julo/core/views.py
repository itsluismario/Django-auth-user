from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, logout as do_logout, login as do_login
from core.forms import UserSignUpForm
from django.shortcuts import redirect


def user_signup(request):

    form = UserSignUpForm()
    # If the user is logged in send to "/"

    if request.method == "POST":
        user_form = UserSignUpForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save(commit=False)
            user.username = user.email
            user.first_name = user.first_name
            user.last_name = user.last_name

            if user.save():
                return render(request,'signup.html',{
                     'form':form,
                     'errors':'The user already exist'
                })
            else:
                user.set_password(user.password)
                user.save()
                userprofile = UserProfile.objects.create(user=user)
                do_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # Redirect to a success page.
                return redirect("/")

        else:
            print(user_form.errors.as_ul)
            return render(request,'signup.html',{
                'form':form,
                'errors':user_form.errors.as_ul
            })



    form = UserSignUpForm()
    return render(request,"signup.html",{
        'form': form
    })
