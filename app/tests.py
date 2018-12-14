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


class TestCreateBlogPageView(TestCase):
    def test_renders_createblog_template(self):
        response = self.client.get(reverse('createblog'))

        self.assertTemplateUsed(response, 'createblog.html')

    def test_provides_form_for_create_blog_page(self):
        response = self.client.get(reverse('createblog'))

        self.assertIsInstance(response.context['form'], forms.CreateBlogForm)


class TestCreateBlogPagePost(TestCase):
    @patch('app.forms.CreateBlogForm')
    @patch('app.models.BlogPost.submit')
    def test_createblog_submitted_with_valid_form(self, submit,
                                                  CreateBlogForm):
        form = CreateBlogForm.return_value
        form.is_valid.return_value = True

        response = self.client.post(reverse('createblog'))

        submit.assert_called_once()

    @patch('app.forms.CreateBlogForm')
    @patch('app.models.BlogPost.submit')
    def test_createblog_does_not_submitted_with_invalid_form(
            self, submit, CreateBlogForm):
        form = CreateBlogForm.return_value
        form.is_valid.return_value = False

        response = self.client.post(reverse('createblog'))

        submit.assert_not_called()
