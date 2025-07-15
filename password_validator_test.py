import unittest
import string

class PasswordValidator:
    def is_valid(self, password: str) -> bool:
        if password is None or len(password) < 8:
            return False

        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        return has_upper and has_lower and has_digit and has_special

class TestPasswordValidator(unittest.TestCase):
    def setUp(self):
        self.validator = PasswordValidator()

    def test_valid_password(self):
        self.assertTrue(self.validator.is_valid("StrongP@ss1"))

    def test_short_password(self):
        self.assertFalse(self.validator.is_valid("S@1a"))

    def test_missing_uppercase(self):
        self.assertFalse(self.validator.is_valid("weakp@ss1"))

    def test_missing_lowercase(self):
        self.assertFalse(self.validator.is_valid("WEAKP@SS1"))

    def test_missing_digit(self):
        self.assertFalse(self.validator.is_valid("WeakP@ss"))

    def test_missing_special_char(self):
        self.assertFalse(self.validator.is_valid("WeakPass1"))

    def test_null_password(self):
        self.assertFalse(self.validator.is_valid(None))

if __name__ == "__main__":
    unittest.main()
