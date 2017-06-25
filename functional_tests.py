from selenium import webdriver
import unittest

# unittest.TestCase를 상속해서 테스트를 클래스 형태로 만든다.
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    # test로 시작하는 메소드는 테스트 메소드이며, 테스트 실행자에 의해서 실행된다.
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browsert.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
