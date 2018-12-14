from django import forms


class CreateBlogForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField()
    author = forms.CharField(max_length=50)
    cover_image_url = forms.URLField()

    # def __str__(self):
    #     return f'ClassBlogForm: {self.title} by {self.author}'

    # def __repr__(self):
    #     return f'<ClassBlogForm {self.title} by {self.author}>'
