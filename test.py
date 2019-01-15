import unittest
from config import get_config
from main import Collector


class TestConfigRelated(unittest.TestCase):
    def test_get_config(self):
        """
        Check if all goes well when a config file can be found
        """
        self.assertIn("log", get_config(filename="sample.ini"))

    def test_get_config_multiple_fields(self):
        """
        Check if function gets other sectors from ini file
        """
        self.assertIn("access_token", get_config(section="GITHUB", filename="sample.ini"))

    def test_get_config_no_file(self):
        """
        Check if fails when no config file can be found
        """
        with self.assertRaises(FileNotFoundError):
            get_config(filename="fail.ini")


class TestCollector(unittest.TestCase):
    def setUp(self):
        self.collector = Collector()
