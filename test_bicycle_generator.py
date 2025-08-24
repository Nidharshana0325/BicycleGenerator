import json
import unittest
from bicycle_generator import generate_bicycle_json

class TestBicycleGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        file_path = r"C:\Nidhieee\projects\BicycleGenerator\Bicycle.xlsx"
        cls.json_str = generate_bicycle_json(file_path)
        cls.data = json.loads(cls.json_str)

    def test_total_count(self):
        self.assertEqual(len(self.data), 5508, "Expected 5508 modifications")

    def test_structure(self):
        for bike in self.data:
            self.assertIn('ID', bike)
            self.assertEqual(bike['Manufacturer'], 'Bikes INC')
            self.assertIn('Brake type', bike)
            self.assertIn('Frame color', bike)
            self.assertIn('Operating temperature', bike)

    def test_specific_bike(self):
        sample_id = 'CITY-R26SSH1-01'
        bike = next((b for b in self.data if b['ID'] == sample_id), None)
        self.assertIsNotNone(bike)
        self.assertEqual(bike['Brake type'], 'Rim')
        self.assertEqual(bike['Wheel diameter'], '26″')
        self.assertEqual(bike['Has suspension'], 'FALSE')
        self.assertEqual(bike['Frame color'], 'RED')
        self.assertEqual(bike['Logo'], 'TRUE')
        self.assertEqual(bike['Operating temperature'], '0 - 40 °C')

    def test_boolean_normalization(self):
        sample_id = 'CITY-R26SSH1-06'
        bike = next((b for b in self.data if b['ID'] == sample_id), None)
        self.assertEqual(bike['Logo'], 'FALSE')

if __name__ == '__main__':
    unittest.main()