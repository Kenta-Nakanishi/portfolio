from django import forms
from .models import customerModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = customerModel

        # formのhtmlに表示させるフィールドを決める。複数ある時、field＝にするとエラーになる。
        fields = ('name', 'email', 'content')
        
        # 各ラベルのタイトルを空文字にしている。''の中に文字を入れたらラベルが表示される
        labels = {
            'name': '',
            'email': '',
            'content': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名前'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
            'content':forms.Textarea(attrs={'class': 'form-control', 'placeholder': '本文'}),
        }