import unittest
from contextlib import redirect_stdout
from io import StringIO

from customer_support_automation import main


class MainTests(unittest.TestCase):
    def test_main_prints_greeting(self) -> None:
        output = StringIO()
        with redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue(), "Hello from customer-support-automation!\n")


if __name__ == "__main__":
    unittest.main()
