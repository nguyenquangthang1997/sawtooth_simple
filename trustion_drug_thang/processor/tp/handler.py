import datetime
import time

from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction

from addressing import addresser

from protobuf import payload_pb2
from protobuf import user_pb2

from tp.payload import SupplyPayload
from tp.state import SupplyState

SYNC_TOLERANCE = 60 * 5

class SupplyHandler(TransactionHandler):

    @property
    def family_name(self):
        return addresser.FAMILY_NAME

    @property
    def family_versions(self):
        return [addresser.FAMILY_VERSION]

    @property
    def namespaces(self):
        return [addresser.NAMESPACE]

    def apply(self, transaction, context):
        header = transaction.header
        payload = SupplyPayload(transaction.payload)
        state = SupplyState(context)

        _validate_timestamp(payload.timestamp)

        if payload.action == payload_pb2.SimpleSupplyPayload.CREATE_USER:
            _create_user(
            state=state,
            public_key=header.signer_public_key,
            payload=payload)
        elif payload.action == payload_pb2.SimpleSupplyPayload.DRUG_IMPORT:
            _drug_import(
                state=state,
                public_key=header.signer_public_key,
                payload=payload
                )
        elif payload.action == payload_pb2.SimpleSupplyPayload.UPDATE_STATUS:
            _update_status(
                state=state,
                public_key=header.signer_public_key,
                payload=payload
                )
        elif payload.action == payload_pb2.SimpleSupplyPayload.UPDATE_LOCATION:
            _update_location(
                state=state,
                public_key=header.signer_public_key,
                payload=payload
                )

def _create_user(state, public_key, payload):
    if state.get_user(public_key):
        raise InvalidTransaction('User with the public key {} already '
                                 'exists'.format(public_key))
    state.set_user(
        public_key=public_key,
        username=payload.data.username,
        role=payload.data.role,
        timestamp=payload.timestamp)

def _drug_import(state,public_key, payload):
    user = state.get_user(public_key)
    if user is None:
        raise InvalidTransaction('User with the public key {} does '
                                 'not exist'.format(public_key))
    if user.role not in [user_pb2.User.PATIENT]:
        raise InvalidTransaction('Permission denied')

    if payload.data.id == '':
        raise InvalidTransaction('No product ID provided')

    if state.get_product(payload.data.id):
        raise InvalidTransaction('Identifier {} belongs to an existing'
                                 'product'.format(payload.data.id))
    state.drug_import(
        timestamp=payload.timestamp,
        id=payload.data.id,
        name=payload.data.name
        )



def _update_status(state, public_key, payload):
    user = state.get_user(public_key)
    product = state.get_product(payload.data.id)
    if product is None:
        raise InvalidTransaction('product with the id {} does not '
                                 'exist'.format(payload.data.id))
    if user is None:
        raise InvalidTransaction('User with the public key {} does '
                                 'not exist'.format(public_key))

    if user.role not in [user_pb2.User.PATIENT]:
        raise InvalidTransaction('Permission denied')

    state.update_status(
        timestamp=payload.timestamp,
        id=payload.data.id,
        quantity=payload.data.quantity,
        price=payload.data.price
    )



def _update_location(state, public_key, payload):
    user = state.get_user(public_key)
    product = state.get_product(payload.data.id)
    if product is None:
        raise InvalidTransaction('product with the id {} does not '
                                 'exist'.format(payload.data.id))
    if user is None:
        raise InvalidTransaction('User with the public key {} does '
                                 'not exist'.format(public_key))

    if user.role not in [user_pb2.User.PATIENT]:
        raise InvalidTransaction('Permission denied')

    state.update_location(
        timestamp=payload.timestamp,
        id=payload.data.id,
        longitude=payload.data.longitude,
        latitude=payload.data.latitude
    )



def _validate_timestamp(timestamp):
    """Validates that the client submitted timestamp for a transaction is not
    greater than current time, within a tolerance defined by SYNC_TOLERANCE

    NOTE: Timestamp validation can be challenging since the machines that are
    submitting and validating transactions may have different system times
    """
    dts = datetime.datetime.utcnow()
    current_time = round(time.mktime(dts.timetuple()) + dts.microsecond/1e6)
    if (timestamp - current_time) > SYNC_TOLERANCE:
        raise InvalidTransaction(
            'Timestamp must be less than local time.'
            ' Expected {0} in ({1}-{2}, {1}+{2})'.format(
                timestamp, current_time, SYNC_TOLERANCE))