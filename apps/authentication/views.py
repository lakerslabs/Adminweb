# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib import messages

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None
    #esta parte recolecta lo de next para hacer la redireccion claro si hay un next
    try:
        meta = request.META['QUERY_STRING'].split('=')[1]
    except IndexError:
        meta = None
    
    # print('Meta: ' + meta)
    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if meta is not None:
                    return redirect(meta)
                else:
                    return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            # Usar messages framework para un mensaje flash
            messages.success(request, 'User created successfully!')
            
            # Redireccionar a login con un flag para mostrar SweetAlert2
            return redirect("/login?next=/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})