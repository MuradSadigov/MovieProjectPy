from unittest import TestCase
from command_processor import cp


class TestCommandProcessor(TestCase):
    def test_parse_command(self):
        user_input = 'l -v -t "test test test 172937123918237912739182791849247182"'

        expected_command = "l"
        expected_switches = {
            "-v": "",
            "-t": "test test test 172937123918237912739182791849247182"
        }

        actual_command, actual_switches = cp.parse_command(user_input)
        
        self.assertEqual(expected_command, actual_command)
        self.assertEqual(expected_switches, actual_switches)
