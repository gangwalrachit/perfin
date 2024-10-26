import grpc
import time

from genproto.transaction_api_pb2_grpc import (
    TransactionAPIStub,
)
from genproto.transaction_api_pb2 import (
    Transaction,
    TransactionType,
)


def run():
    host = "localhost"
    port = 50051
    channel = grpc.insecure_channel("{}:{}".format(host, port))
    stub = TransactionAPIStub(channel)

    request = Transaction(
        id="123456789",
        type=TransactionType.TRANSACTION_TYPE_CREDIT,
        amount=100,
        sender="user1",
        receiver="user2",
        timestamp={"seconds": int(time.time())},
        user={"id": "username", "first_name": "FIRST", "last_name": "LAST"},
    )
    print(f"Sending request:\n{request}")

    response = stub.InsertTransaction(request)
    print(f"Received response:\n{response}")


if __name__ == "__main__":
    run()
