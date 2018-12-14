from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from app import forms


class TestHomePageView(TestCase):
    def test_renders_home_template(self):
        response = self.client.get(reverse('home'))

        self.assertTemplateUsed(response, 'home.html')

    @patch('app.models.BlogPost.ordered_blogposts')
    def test_shows_recent_blog_post(self, ordered_blogposts):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.context['blogposts'],
                         ordered_blogposts.return_value)


class TestCreateBlogPage(TestCase):
    def test_renders_createblog_template(self):
        response = self.client.get(reverse('createblog'))

        self.assertTemplateUsed(response, 'createblog.html')

    def test_provides_form_for_create_blog_page(self):
        response = self.client.get(reverse('createblog'))

        self.assertIsInstance(response.context['form'], forms.CreateBlogForm)
