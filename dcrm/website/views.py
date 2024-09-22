from django.shortcuts import render

#13 - Define homepage view
def home(request):
    return render(request, 'home.html', {}) #14 - Pass an empty focus Python dict {}
