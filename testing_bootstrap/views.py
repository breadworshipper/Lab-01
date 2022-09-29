from django.shortcuts import render

# Create your views here.
def show_bootstrap_testing(request):
    return render(request, 'bootstrap_testing.html')
