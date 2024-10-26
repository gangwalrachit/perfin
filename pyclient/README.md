## Generating proto code

Steps to do this and get the requried relative imports:

1. From `perfin` run `cp protos/transaction_api.proto service/genproto/`
2. Then `cd service/`
3. Finally run `venv/bin/python3 -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. genproto/transaction_api.proto`

Note: Make sure you have setup venv from the requirements
