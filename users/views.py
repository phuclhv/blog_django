from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    # Check if value the user input is valid or net
    if form.is_valid():
      # Save the user to the database
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}!')
      return redirect('blog-home') 
  else:
    form = UserRegisterForm(),
  
  context = {
    'form': form
  }

  return render(request, 'users/register.html', context)

