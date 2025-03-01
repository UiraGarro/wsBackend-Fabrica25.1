from django import forms

class NewsForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=30)
    email = forms.EmailField(label='E-mail')
    telefone = forms.CharField(label='Telefone', max_length=15)
    idade = forms.CharField(label='Idade', max_length=3)
    cidade = forms.CharField(label='Cidade', max_length=30)
    estado = forms.CharField(label='Estado', max_length=2)
    pais = forms.CharField(label='País', max_length=30)