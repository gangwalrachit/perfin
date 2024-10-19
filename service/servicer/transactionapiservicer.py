import logging

from genproto.transaction.transaction_api_pb2_grpc import (
    TransactionAPIServicer,
)
from genproto.transaction.transaction_api_pb2 import (
    Operation,
    TransactionResponse,
    TransactionStatus,
)


LOGGER = logging.getLogger(__name__)


class TransactionAPIServicer(TransactionAPIServicer):
    """
    Class to start the transaction API servicer.
    """

    def InsertTransaction(self, request, context):
        """Insert transaction

        :param request: Request received.
        :param context: Context???
        """
        LOGGER.info(f"Received request:\n{request}")
        self.process_request(request)

        return TransactionResponse(
            id=request.id,
            type=request.type,
            operation=Operation.OPERATION_INSERT,
            status=TransactionStatus.TRANSACTION_STATUS_SUCCESS,
        )

    def process_request(self, request):
        """
        Process the request

        :param request: Request received.
        """
        # TODO: add request details to a fixed storage
        LOGGER.info("Request processed successfully!")
