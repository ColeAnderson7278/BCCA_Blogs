from django.shortcuts import render, redirect
from django.views import View
from app import models
from app import forms


class HomePage(View):
    def get(self, request):
        return render(request, "home.html",
                      {'blogposts': models.BlogPost.ordered_blogposts()})


class CreateBlogPage(View):
    def get(self, request):
        return render(request, 'createblog.html',
                      {'form': forms.CreateBlogForm()})

    def post(self, request):
        form = forms.CreateBlogForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            author = form.cleaned_data['author']
            cover_image_url = form.cleaned_data['cover_image_url']
            models.BlogPost.submit(title, body, author, cover_image_url)
            return redirect('home')
        return render(request, 'createblog.html', {'form': form})
