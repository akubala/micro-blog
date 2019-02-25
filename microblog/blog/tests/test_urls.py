from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
    PostListView,
    UserPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    about_view
)


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.blog_home_url = reverse('blog-home')
        self.user_post_list_url = reverse('user-posts', args=['username'])
        self.post_detail_url = reverse('post-detail', args=[1])
        self.post_create_url = reverse('post-create')
        self.post_update_url = reverse('post-update', args=[1])
        self.post_delete_url = reverse('post-delete', args=[1])
        self.blog_about_url = reverse('blog-about')

    def test_post_list_view_url_resolves(self):
        self.assertEqual(resolve(self.blog_home_url).func.view_class, PostListView)

    def test_user_post_list_view_url_resolves(self):
        self.assertEqual(resolve(self.user_post_list_url).func.view_class, UserPostListView)

    def test_post_detail_view_url_resolves(self):
        self.assertEqual(resolve(self.post_detail_url).func.view_class, PostDetailView)

    def test_post_create_view_url_resolves(self):
        self.assertEqual(resolve(self.post_create_url).func.view_class, PostCreateView)

    def test_post_update_view_url_resolves(self):
        self.assertEqual(resolve(self.post_update_url).func.view_class, PostUpdateView)

    def test_post_delete_view_url_resolves(self):
        self.assertEqual(resolve(self.post_delete_url).func.view_class, PostDeleteView)

    def test_about_url_resolves(self):
        self.assertEqual(resolve(self.blog_about_url).func, about_view)
