from buf.validate import validator
from buf.validate.conformance import runner
from buf.validate.conformance.cases import numbers_pb2
import unittest


# Test basic validation
class TestValidate(unittest.TestCase):
    def test_SFixed64ExLTGT(self):
        msg = numbers_pb2.SFixed64ExLTGT(val=11)
        violations = validator.validate(msg)
        self.assertEqual(len(violations.violations), 0)


if __name__ == "__main__":
    unittest.main()
