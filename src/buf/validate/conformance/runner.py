import sys

from buf import validate
from buf.validate.conformance.harness import harness_pb2
from google.protobuf import any_pb2
from google.protobuf import descriptor_pool
from google.protobuf import descriptor
from google.protobuf import message_factory


def RunTestCase(tc: any, result: harness_pb2.TestResult):
    # Run the validator
    validate.validate(tc, result.validation_error)
    if len(result.validation_error.violations) == 0:
        result.success = True


def RunConformanceTest(
    request: harness_pb2.TestConformanceRequest,
) -> harness_pb2.TestConformanceResponse:
    pool = descriptor_pool.DescriptorPool()
    for fd in request.fdset.file:
        pool.Add(fd)
    result = harness_pb2.TestConformanceResponse()
    for name, tc in request.cases.items():
        type_name = tc.type_url.split("/")[-1]
        desc: descriptor.Descriptor = pool.FindMessageTypeByName(type_name)
        # Create a message from the protobuf descriptor
        msg = message_factory.GetMessageClass(desc)()
        tc.Unpack(msg)
        RunTestCase(msg, result.results[name])
    return result


if __name__ == "__main__":
    # Read a serialized TestConformanceRequest from stdin
    request = harness_pb2.TestConformanceRequest()
    request.ParseFromString(sys.stdin.buffer.read())
    # Run the test
    result = RunConformanceTest(request)
    # Write a serialized TestConformanceResponse to stdout
    sys.stdout.buffer.write(result.SerializeToString())
    sys.stdout.flush()
    sys.exit(0)
