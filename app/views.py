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
