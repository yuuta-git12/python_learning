import unittest
from models import robot
import string

class RobotTest(unittest.TestCase):
    def test_hello(self):
        test_robot = robot.Robot()
        self.assertEqual('testresult', test_robot.hello())
    

if __name__ == "__main__":
    unittest.main()
