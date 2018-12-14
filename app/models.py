from django.db import models


class BlogPost(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cover_image_url = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.author}'

    @staticmethod
    def ordered_blogposts():
        return BlogPost.objects.all().order_by('-date')

    @staticmethod
    def submit(title, body, author, cover_image_url):
        BlogPost(
            title=title,
            body=body,
            author=author,
            cover_image_url=cover_image_url).save()


class Comment(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title} by {self.author}'
