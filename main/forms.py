from django.forms import ModelForm
from main.models import Post, Contato

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['post_title', 'post_content']
