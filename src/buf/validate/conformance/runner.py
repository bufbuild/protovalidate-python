import sys

from buf import validate
from buf.validate.conformance.harness import results_pb2
from buf.validate.conformance.harness import harness_pb2


def RunConformanceTest(
    request: harness_pb2.TestConformanceRequest,
) -> harness_pb2.TestConformanceResponse:
    result = harness_pb2.TestConformanceResponse()
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
