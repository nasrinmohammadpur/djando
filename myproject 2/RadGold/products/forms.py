#from django import forms
from django import forms


#class ImageForm(forms.Form):
      #  name = forms.CharField()
      #  image = forms.ImageField()


class EmailPostForm(forms.Form):
      name = forms.CharField(max_length=25)
      email = forms.EmailField()
      to = forms.EmailField()
      comments = forms.CharField(required=False,
                                   widget=forms.Textarea)