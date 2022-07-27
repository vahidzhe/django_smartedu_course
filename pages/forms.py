from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
   

    def __init__(self, *args, **kwargs):
        super(ContactForm,self).__init__(*args, **kwargs)

        


        self.fields['first_name'].widget.attrs={'placeholder':'First Name','class':'form-control'}
        self.fields['last_name'].widget.attrs={'placeholder':'Last Name','class':'form-control'}
        self.fields['email'].widget.attrs={'placeholder':'Email','class':'form-control'}
        self.fields['phone'].widget.attrs={'placeholder':'Phone','class':'form-control'}
        self.fields['text'].widget.attrs={'placeholder':'Text','class':'form-control'}

    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','phone','text']