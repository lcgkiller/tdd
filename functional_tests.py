from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')

        # 엔터키를 치면 페이지가 갱신되면서 작업 목록에 "1: 공작깃털 사기" 아이템이 추가된다.
        # Keys 클래스는 Enter나 Ctrl같은 특수 키 입력을 전송하는 역할을 한다.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
