from django.shortcuts import render, HttpResponseRedirect


from django.contrib.auth import login

from .forms import CustomUserCreationForm

# Create your views here.


def register_user(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = CustomUserCreationForm()
        print(form.errors)

    return render(request, 'core/register.html', {'form': form})
