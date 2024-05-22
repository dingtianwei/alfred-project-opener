import unittest
from src import search


class TestGetConfig(unittest.TestCase):
    def test_get_config(self):
        self.assertIn("grand_list",search.get_config("~/.alfred_project_opener.json") )


if __name__ == '__main__':
    unittest.main()
