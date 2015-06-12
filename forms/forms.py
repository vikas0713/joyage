from django import forms
from models import *
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit, Layout, Div, ButtonHolder
#from crispy_forms.bootstrap import FormActions


class RegisterForm(forms.ModelForm):
    
    
    class Meta:
        model=FormsModel
        exclude=['created_at']
        
    def __init__(self , *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'id':'datepicker'
                                                 })
        self.fields['time'].widget.attrs.update({'class':'form-control',
                                                 'data-field':'time'
                                                 })
        self.fields['website'].widget.attrs.update({'placeholder':'Add http:// first',
                                                 })