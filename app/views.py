from django.shortcuts import render, redirect
from django.views import View
from app import models


class HomePage(View):
    def get(self, request):
        return render(request, "home.html",
                      {'blogposts': models.BlogPost.ordered_blogposts()})
