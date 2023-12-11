from unittest import TestCase
from helpers import *


class TestHelpers(TestCase):
    def test_minutes_to_time_format(self):
        length_in_min = 180

        result = minutes_to_time_format(length_in_min)
        self.assertEqual(result, "03:00")
        self.assertNotEqual(result, "03:01")

    def test_time_format_to_minutes(self):
        length_in_time_format = "04:59"

        result = time_format_to_minutes(length_in_time_format)

        self.assertEqual(result, 299)
        self.assertNotEqual(result, 298)

    def test_is_valid_year(self):
        years_in_str = ["2000", "2003", "2000", "1999", "1800", "1850"]
        years_in_str_Falsy = ["200d3", "20-33", "01-01-2001"]

        for year in years_in_str:
            result = is_valid_year(year)
            self.assertEqual(result, True)
            
        for year in years_in_str_Falsy:
            result = is_valid_year(year)
            self.assertEqual(result, False)
            
    def test_is_valid_time_format(self):
        time_formats = ["01:21", "00:01", "99:59", "12:12", "00:00"]
        
        for time in time_formats:
            result = is_valid_time_format(time)
            self.assertEqual(result, True)
        
