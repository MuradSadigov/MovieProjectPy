from unittest import TextTestRunner, TestLoader, TestSuite
from tests.command_processor_test import TestCommandProcessor

from tests.helpers_test import TestHelpers


if __name__ == "__main__":
    runner = TextTestRunner()
    test_suite = TestSuite()
    test_loader = TestLoader()
    
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestHelpers))
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestCommandProcessor))
    
    runner.run(test_suite)
