import unittest
import requests
from stattleship.stattleship import Stattleship


class StattleshipTestCase(unittest.TestCase):

    stattleship = Stattleship()

    def test_get_data_endpoint(self):

        with self.assertRaises(requests.exceptions.HTTPError):
            self.stattleship.get_data(
            	sport='foo', 
            	league='bar', 
            	data_type='foobar'
            )

    def test_get_data_credentials(self):

        with self.assertRaises(requests.exceptions.HTTPError):
            self.stattleship.get_data(
            	sport='basketball', 
            	league='nba', 
            	data_type='players'
            )

    def tear_down(self):
        self.stattleship = None
