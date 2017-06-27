from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


# unittest.TestCase를 상속해서 테스트를 클래스 형태로 만든다.
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    # 헬퍼메소드
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    # test로 시작하는 메소드는 테스트 메소드이며, 테스트 실행자에 의해서 실행된다.
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("공작깃털을 이용해서 그물만들기")
        inputbox.send_keys(Keys.ENTER)
        # 페이지를 다시 갱신되고, 두 개의 아이템이 목록에 보인다.

        self.check_for_row_in_list_table('1: 공작깃털 사기')
        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물만들기')

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
