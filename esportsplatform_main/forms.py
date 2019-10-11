from django import forms
from .models import *

class Cmopetition_info_Form(forms.ModelForm):
    class Meta:
        model = Cmopetition_info
        fields = ('c_contact', 'c_rule', 'c_rule_file', 'c_prize', 'c_schedule')
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['c_rule_file'].required = False
