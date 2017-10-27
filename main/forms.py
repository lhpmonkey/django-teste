from django.forms import ModelForm
from main.models import Post, Contato
from django import forms

class PostForm(forms.ModelForm):
	
	post_title= forms.CharField(label="Titulo do Post", widget= forms.TextInput(attrs={'class': 'form-control col-md-4', 'placeholder': 'Titulo do Post aqui'}))
	post_content = forms.CharField(label="Conteudo do Post", widget= forms.Textarea(attrs={'class': 'form-control col-md-6', 'placeholder': 'Conteudo da noticia'}))
	
	class Meta:
		model = Post
		fields = ['post_title', 'post_content']
