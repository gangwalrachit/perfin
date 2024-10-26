import grpc
import logging

from genproto.transaction_api_pb2_grpc import (
    TransactionAPIServicer,
)
from genproto.transaction_api_pb2 import (
    Operation,
    Transaction,
    TransactionResponse,
    TransactionStatus,
)


LOG = logging.getLogger(__name__)


class TransactionAPIServicer(TransactionAPIServicer):
    """
    Class to start the transaction API servicer.
    """

    def InsertTransaction(
        self, request: Transaction, context: grpc.ServicerContext
    ) -> TransactionResponse:
        """
        Insert transaction

        :param request: Request received.
        :param context: Context to manage state and properties of an RPC.
        """
        LOG.info(type(context))
        LOG.info(context)
        LOG.info(f"Received request:\n{request}")
        self.process_request(request)

        return TransactionResponse(
            id=request.id,
            type=request.type,
            operation=Operation.OPERATION_INSERT,
            status=TransactionStatus.TRANSACTION_STATUS_SUCCESS,
        )

    def process_request(self, request: Transaction) -> None:
        """
        Process the request

        :param request: Request received.
        """
        # TODO: add request details to a fixed storage
        LOG.info("Request processed successfully!")
