import unittest
from app import add
class TestApp(unittest.TestCase):
    def testadd(self):
        self.assertEquals(add(10,20),30);
if __name__=="__main__":
    unittest.main();