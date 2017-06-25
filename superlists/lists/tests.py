from django.http import HttpRequest
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

        self.assertTrue(response.content.startswith(b'<html>'))  # 응답내용이 html로 시작해서 html로 끝나는지 확인
        self.assertIn(b'<title>To-Do lists</title>', response.content)  # 타이틀 태그에 To-Do lists라는 단어가 있는지 확인
        self.assertTrue(response.content.endswith(b'</html>'))
