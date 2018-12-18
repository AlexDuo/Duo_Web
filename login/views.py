from django.shortcuts import render

from .forms import login_form
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = login_form
        if form.is_valid():
            return render(request,'success.html')
        else:
            return render(request,'login.html',{'form':form})
    else:
        form = login_form
        return render(request,'login.html',{'form':form})
