from django.shortcuts import render, redirect #37 - import redirect function.
from django.contrib.auth import authenticate, login, logout #25 - Import Django Authentication.
from django.contrib import messages #26 - Flash successfull messages for login, logout, and registration.
from .forms import SignUpForm # 55 - Import form just created in website/forms.py file.
from .models import Record #73 - Import Record data. 



#13 - Define homepage view
def home(request):
    
    #72 - View Model data on the homepage after logged in.
    records = Record.objects.all()
    
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
        return render(request, 'home.html', {'records':records}) #14 - Pass an empty focus Python dict {}.
    #74 - If the user is already logged in we can pass in the records variable to the homepage so they can view the list of Records. 

#27 - Define logout views.
def logout_user(request):
    logout(request) #39 - Logout function by import
    messages.success(request, 'You have been successfully logged out!')
    return(redirect('home'))

#44 - Define Register User.
def register_user(request):
    if request.method == 'POST': #56 - Someone filling out our SignUpForm its POST method.
        form = SignUpForm(request.POST)
        if form.is_valid(): #57 - Find out if what the user put in the form is valid.
            form.save()
            #58 - Authenticate and login.
            username = form.cleaned_data['username'] #59 - form.cleaned_data takes whatever they posted on the form and assigns to the username variable.
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'You have successfully registered as a new user! Welcome {username}!') # Using the f-string 'formatted string literal' to have Python replace {username} with the value of the username variable. 
            return redirect('home')
    else:
        form = SignUpForm() #60 - No need to pass in a request.POST, because the user has not filled out the form yet. 
        return render(request, 'register.html', {'form':form}) #61 - Pass in the SignUpForm into the webpage. 
    
    return render(request, 'register.html', {'form':form}) #67 - Handle the Error on webpage with register.html error code. 
