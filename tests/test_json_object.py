import unittest
import json
from jsonobject.JsonObject import JsonObject


class TestJsonObject(unittest.TestCase):

    def setUp(self):
        self.json = JsonObject({
            "value": 5000,
            "id_performance": 2,
            "performance": "2",
            "id_lock": 2,
            "lock": "2",
            "sector": "s2"
        })

    def test_init(self):
        self.assertIsInstance(self.json, JsonObject)

    def test_to_json(self):
        data = self.json.toJson()
        self.assertTrue(self.is_json(data))

    def test_values(self):
        values = self.json.values()
        expected_values = [5000, 2, '2', 2, '2', 's2']
        self.assertTrue(list(values) == expected_values)

    def test_keys(self):
        keys = self.json.keys()
        expected_keys = [
            'value',
            'id_performance',
            'performance',
            'id_lock',
            'lock',
            'sector'
        ]
        self.assertTrue(list(keys) == expected_keys)

    def test_items(self):
        items = self.json.items()
        print(items)
        expected_items = [
            ('value', 5000),
            ('id_performance', 2),
            ('performance', '2'),
            ('id_lock', 2),
            ('lock', '2'),
            ('sector', 's2')
        ]
        self.assertTrue(list(items) == expected_items)

    def test_deepcopy(self):
        copy = self.json.deepcopy()
        self.assertIsInstance(copy, JsonObject)

    def is_json(self, data):
        try:
            json_object = json.loads(data)
        except ValueError:
            return False
        return True
