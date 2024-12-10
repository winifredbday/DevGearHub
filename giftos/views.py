from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def create_superuser(request):
    password = "testing321"
    if User.objects.filter(email='admin@devgearhub.com').exists():
        return redirect("homepage")
    User.objects.create_superuser(username="admin", email='admin@devgearhub.com', password=password)
    user = User.objects.get(email='admin@devgearhub.com')
    user.set_password(password)
    user.save()
    return redirect("homepage")