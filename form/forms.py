from django import forms
from .models import Pessoa, Contato, Experiencia, Formacao
from django.forms import modelformset_factory




class formularioContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('email', 'telefone','cidade', 'endereco', 'numero')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;', 'placeholder': 'exemplo@email.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;', 'placeholder': '(xx)xxxxx-xxxx'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
            'numero': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
        }
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if Contato.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Este email já está em uso.")
            return email

        def clean_telefone(self):
            telefone = self.cleaned_data.get('telefone')
            if Contato.objects.filter(telefone=telefone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Este telefone já está em uso.")
            return telefone

class formularioCadastro(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'data_nascimento', 'genero')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;', 'placeholder': 'Nome completo'}),
            'data_nascimento': forms.DateInput(format='%d-%m-%y', attrs={'class': 'form-control-sm', 'type': 'date', 'style': 'border-radius: 10px;'}),
        }

class formularioExperiencia(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ('empresa', 'cargo', 'duracao', 'resumo')
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
            'duracao': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
            'resumo': forms.TextInput(attrs={'class': 'form-control-sm','style': 'border-radius: 10px;'}),
        }

class formularioFormacao(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ('instituicao', 'curso', 'periodo')
        widgets = {
            'instituicao': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
            'curso': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
            'periodo': forms.TextInput(attrs={'class': 'form-control-sm', 'style': 'border-radius: 10px;'}),
        }

ExperienciaFormSet = modelformset_factory(Experiencia, form=formularioExperiencia, extra=1)
FormacaoFormSet = modelformset_factory(Formacao, form=formularioFormacao, extra=1)