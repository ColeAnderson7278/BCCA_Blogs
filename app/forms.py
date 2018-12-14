from django import forms


class CreateBlogForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField()
    author = forms.CharField(max_length=50)
    cover_image_url = forms.CharField()
