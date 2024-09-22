from django.shortcuts import render, redirect #37 - import redirect function.
from django.contrib.auth import authenticate, login, logout #25 - Import Django Authentication.
from django.contrib import messages #26 - Flash successfull messages for login, logout, and registration.



#13 - Define homepage view
def home(request):
    
    #34 - Check to see if logging in. If logging in = posting.
    if request.method == 'POST':
        username = request.POST['username'] #35 - Assign whatever is typed in form into variables created with username and password.
        password = request.POST['password']
        
        #36 - Authenticate.
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been successfully logged in!')
            return(redirect('home'))
        else:
            messages.success(request, 'There was an error logging in, please try again...')
            return(redirect('home'))
    else: #If not logging in, and just going to the page they are getting.
        return render(request, 'home.html', {}) #14 - Pass an empty focus Python dict {}.

#27 - Define logout views.
def logout_user(request):
    logout(request) #39 - Logout function by import
    messages.success(request, 'You have been successfully logged out!')
    return(redirect('home'))
