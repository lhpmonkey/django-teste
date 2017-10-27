from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Contato, Post
from main.forms import PostForm

# Create your views here.

def index(request):
	lista = Post.objects.all()
	return render(request,"index.html", {'lista': lista})

def deletar(request, id):
	poster = Post.objects.filter(post_id=id)
	poster.delete()

	return redirect(index)

def atualizar(request, id):
	poster = Post.objects.get(post_id=id)
	form = PostForm(request.POST or None, instance= poster)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(index)
	return render(request, 'novo.html', {'form': form, 'id': id})

def novo(request):
	form = PostForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect(index)

	return render(request,"novo.html", {'form': form})


