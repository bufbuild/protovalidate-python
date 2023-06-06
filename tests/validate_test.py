from buf.validate import validator
from buf.validate.conformance.cases import bool_pb2
from buf.validate.conformance import runner
import unittest


# Test basic validation
class TestValidate(unittest.TestCase):
    def test_int32(self):
        msg = bool_pb2.BoolConstTrue(val=True)
        violations = validator.validate(msg)
        result = runner.RunTestCase(msg)
        self.assertEqual(len(violations.violations), 0)


if __name__ == "__main__":
    unittest.main()
