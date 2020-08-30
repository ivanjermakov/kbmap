from unittest import TestCase

from test.util import *


class ActionTest(TestCase):

    def assert_mapping(self, config, keys, result):
        self.assertEqual(simulate_keys(config, keys), result)
