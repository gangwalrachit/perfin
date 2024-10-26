## Generating proto code

Steps to do this and get the requried relative imports:

1. From `perfin` run `cp protos/transaction_api.proto service/genproto/`
2. Then `cd service/`
3. Finally run `venv/bin/python3 -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. genproto/transaction_api.proto`

Note: Make sure you have setup venv from the requirements

## Implemmenting a python client

```python
import grpc
import time

from genproto.transaction.transaction_api_pb2_grpc import (
    TransactionAPIStub,
)
from genproto.transaction.transaction_api_pb2 import (
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
```
