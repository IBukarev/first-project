from .models import Online
from django.forms import ModelForm,TextInput,Textarea



class OnlineForm(ModelForm):
    class Meta:
        model = Online
        fields=['name','sms']
        widgets = {
            'name':TextInput(attrs={
                'class':'online_input_name',
                'placeholder':'Как тебя зовут?'
        }),
            'sms':Textarea(attrs={
                'class':'online_input_sms',
                'placeholder':'Введите сообщение'
            })
        }