import unittest
import views.console as console
import string

class ConsoleTest(unittest.TestCase):
    def test_find_template_path(self):
        # self.assertEqual('/usr/src/app/roboter/templates', console.get_template_dir_path())
        self.assertEqual('/usr/src/app/roboter/templates/template_recommend.txt', console.find_template('template_recommend.txt'))
    def test_get_template(self):
        self.assertEqual('template_hello', console.get_template('template_hello.txt').substitute())
        self.assertEqual('template_hello', console.get_template('template_like_restaurant.txt').substitute(name1='Yuta'))
        # self.assertEqual('template_hello', console.get_template('template_recommend.txt'))
        # self.assertEqual('template_hello', console.get_template('template_thank_you.txt'))


if __name__ == "__main__":
    unittest.main()

