from django.shortcuts import render, redirect #37 - import redirect function.
from django.contrib.auth import authenticate, login, logout #25 - Import Django Authentication.
from django.contrib import messages #26 - Flash successfull messages for login, logout, and registration.
from .forms import SignUpForm, AddRecordForm # 55 - Import form just created in website/forms.py file.                  #105 - import the AddRecordForm so it can be used.
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

#82 - Define customer_record corresponding with primary keys.
def customer_record(request, pk):
    #83 - Check if person is logged in first.
    if request.user.is_authenticated:
        #84 - Then look up the record.
        customer_record = Record.objects.get(id=pk) # Call a single record with Record.objects.get(id=pk) and pass on the variables of id attached to a pk. 
        return render(request, 'record.html', {'customer_record':customer_record}) #85 
    else: 
        messages.success(request, 'Sorry, you must be logged in to view that page.') #86
        return redirect('home')
    
#95 - Define delete_customer corresponding with primary keys of record we want to delete.
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record has been deleted successfully.')
        return(redirect('home'))
    else:
        messages.success(request, 'Sorry, you must be logged in to delete Records.')
        return(redirect('home'))
        
#98 - Define add record function
def add_record(request):
    form = AddRecordForm(request.POST or None) #106 - Are they adding a new record(posting), and if not just go to the webpage.
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'New customer record added.')
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, 'Sorry, you must be logged in to create a new customer record.')
        return(redirect('home'))
    
#109 - Define update record function
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk) #110 - Assign the record according to the id and primary key and assign it this variable current_record.
        
        form = AddRecordForm(request.POST or None, instance=current_record) #111 - Pass an instance of the current_record with the primary key we have passed into the page, by passing it back into the page with an instance of itself.
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer Record has been updated!')
            return(redirect('home'))
        return render(request, 'update_record.html', {'form':form}) #112
    else: 
        messages.success(request, 'Sorry, you must be logged in to update a customer record.')
        return(redirect('home'))
             