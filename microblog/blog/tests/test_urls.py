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

    def test_post_list_view_url_resolves(self):
        url = reverse('blog-home')
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_user_post_list_view_url_resolves(self):
        url = reverse('user-posts', args=['username'])
        self.assertEqual(resolve(url).func.view_class, UserPostListView)

    def test_post_detail_view_url_resolves(self):
        url = reverse('post-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_post_create_view_url_resolves(self):
        url = reverse('post-create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

    def test_post_update_view_url_resolves(self):
        url = reverse('post-update', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostUpdateView)

    def test_post_delete_view_url_resolves(self):
        url = reverse('post-delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDeleteView)

    def test_about_url_resolves(self):
        url = reverse('blog-about')
        self.assertEqual(resolve(url).func, about_view)
