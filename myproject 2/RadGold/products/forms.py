#from django import forms
from django import forms
from .models import Comment
#from django import forms
#from uploads.core.models import Document
 
#class DocumentForm(forms.ModelForm):
    #class Meta:
    #    model = Document
    #    fields = ('document_addr' )

#class ImageForm(forms.Form):
      #  name = forms.CharField()
      #  image = forms.ImageField()


class EmailPostForm(forms.Form):
      name = forms.CharField(max_length=25)
      email = forms.EmailField()
      to = forms.EmailField()
      comments = forms.CharField(required=False,
                                   widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
      model = Comment
      fields = ('name', 'email', 'body')                                   