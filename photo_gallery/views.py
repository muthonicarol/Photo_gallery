from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.forms import UserCreationForm  
from.forms import PhotoForms , Userforms 
from.models import Photo





def register(request):
    if request.method =='POST': #checks whether the user has submitted a form,
        form = UserCreationForm(request.POST) # if the request is post a form is created that helps the user to create an account
        if form.is_valid: # this one validates if the user has entered the data according to the form fields
            form.save()  # if the form is valid then its saved
            return redirect('register') # the user is redirected to the login page
    else :
       form = UserCreationForm() # if the request is not POST 
    return render (request,'register.html', {'form':form}) #this one will display a restration form to the user


@login_required # checks whether the user is logged in
def profile(request):
    user = request.user # returns the user instance that is currently logged in
    return render (request, 'profile.html',{'user':user}) #


@login_required #checks whether the user is logged in
def Upload_photo (request):
    if request.method == 'POST':
        form = PhotoForms (request. POST, request.files) #allows the user to upload a file
        if form.is_valid(): #checks whether the data entered is valid according to the form fields
            photo = form.save (commit= False)
            photo.user = request.user
            photo.save()
            return redirect ('photo_list')
    else:
        form = PhotoForms()
    return render (request, 'upload_photo.html', {'form' : form})   

def photo_list(request):  
   photos = Photo.objects.all()  
   return render(request, 'photo_list.html', {'photos': photos})  
  


 
        
     



  


 