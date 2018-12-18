from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import register_form
from register import models
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            models.user_info_entity.objects.create(username=username,password=password,email=email)
            return render(request,'success.html')
    else:
        form = register_form
        return render(request,'register.html',{'form':form})
    return render(request, 'register.html', {'form': form})


