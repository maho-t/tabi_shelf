import imp
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import AccountsCreationForm
from django.urls import is_valid_path

def register(request):
  if request.method != 'POST':
    form = AccountsCreationForm()
  else:
    form = AccountsCreationForm(data=request.POST)
    if form.is_valid():
      new_user = form.save()
      login(request, new_user)
      return redirect('shelves:index')

  context = {'form': form}
  return render(request, 'registration/register.html', context)