from buf import validate
import unittest

# Test basic validation
class TestValidate(unittest.TestCase):
    def test_basic(self):
        actual = validate.validate(None)
        self.assertEqual(len(actual.violations), 1)
        self.assertEqual(actual.violations[0].constraint_id, 'unimplemented')
        self.assertEqual(actual.violations[0].message, 'Unimplemented')


if __name__ == '__main__':
    unittest.main()
