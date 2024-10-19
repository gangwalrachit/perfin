import grpc
import logging

from concurrent import futures

from genproto.transaction.transaction_api_pb2_grpc import (
    add_TransactionAPIServicer_to_server,
)
from servicer.transactionapiservicer import TransactionAPIServicer


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] :: %(name)s :: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %Z",
)
LOGGER = logging.getLogger(__name__)


def serve():
    LOGGER.info("Serving...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TransactionAPIServicer_to_server(TransactionAPIServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
