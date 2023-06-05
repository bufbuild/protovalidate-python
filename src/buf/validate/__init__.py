from buf.validate import internal as _buf_validate_internal
from buf.validate import expression_pb2
from google.protobuf import message


class Validator:
    def validate(self, message: message.Message) -> expression_pb2.Violations:
        result = expression_pb2.Violations()
        result.violations.append(
            expression_pb2.Violation(
                constraint_id="unimplemented",
                message="Unimplemented",
            )
        )
        return result


_validator = Validator()
validate = _validator.validate
