from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Category, Post


class Test_Create_Post(TestCase):
    @classmethod
    def SetUpTestData(cls):
        test_user = User.objects.create_user(
            username='test_user1', password='password')
        test_category = Category.objects.create(category_name='django')
        test_post = Post.objects.create(category_id=1, title='Post title', excerpt='Post excerpt', description='Post description', slug='Post slug', author_id=1, status='published')


    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        description = f'{post.description}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post title')
        self.assertEqual(description, 'Post description')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post title")

