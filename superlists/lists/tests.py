from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

# Create your tests here.
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # HttpRequest 객체 생성
        response = home_page(request)  # home_page 뷰에 위 객체를 전달해 응답(response)을 얻는다.
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
