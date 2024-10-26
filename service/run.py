import grpc
import logging
import signal
import sys
import threading
import time

from concurrent import futures

from genproto.transaction_api_pb2_grpc import (
    add_TransactionAPIServicer_to_server,
)
from servicer.transactionapiservicer import TransactionAPIServicer


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s :: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %Z",
)
LOG = logging.getLogger(__name__)


def start_heartbeat(interval: int) -> threading.Thread:
    """
    Starts the heartbeat thread that logs the server status.

    :param interval: Heartbeat interval in seconds
    :return: The heartbeat thread
    """

    def heartbeat():
        while True:
            LOG.info("HEARTBEAT")
            time.sleep(interval)

    heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
    heartbeat_thread.start()
    return heartbeat_thread


def shutdown(server: grpc.server) -> None:
    """
    Handles graceful shutdown of the server and heartbeat thread.

    :param server:
    """
    LOG.info("Received shutdown signal. Shutting down server...")
    server.stop(grace=5).wait()  # Gracefully stop the gRPC server
    LOG.info("Server execution complete.")
    sys.exit(0)  # Exit the program


def serve() -> None:
    """
    Main function to start the gRPC server.
    """
    port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TransactionAPIServicer_to_server(TransactionAPIServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    LOG.info(f"Serving on port {port}...")

    # Start the heartbeat thread
    start_heartbeat(30)

    # Register the shutdown function for SIGINT (Ctrl+C) and SIGTERM
    signal.signal(signal.SIGINT, lambda signum, frame: shutdown(server))
    signal.signal(signal.SIGTERM, lambda signum, frame: shutdown(server))

    # Keep the server running and wait for termination signals
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
