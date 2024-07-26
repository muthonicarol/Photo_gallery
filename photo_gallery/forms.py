from django import forms
from photo_gallery.models import User, Photo

class Userforms(forms.ModelForm):
    class Meta:
        model = User # tis one shows that the form is associated with the user class inside the models.py
        fields = ('username', 'email', 'password', 'profile_picture', 'bio') # this are the fields that will be included in the form

class PhotoForms(forms.ModelForm):
    class Meta:
        model = Photo #this one shows that the form is associated with the photo class inside the models.py
        fields = ('title', 'description',  'tags') # this are the fields that will be included in the form


            
