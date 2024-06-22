from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="chrollo", email="chrollo@gmail.com", password="chrollo123")
        cls.post = Post.objects.create(title="test post", body="This is test body", author=cls.user)
        
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "chrollo")
        self.assertEqual(self.post.title, "test post")
        self.assertEqual(self.post.body, "This is test body")
        self.assertEqual(str(self.post), "test post")
