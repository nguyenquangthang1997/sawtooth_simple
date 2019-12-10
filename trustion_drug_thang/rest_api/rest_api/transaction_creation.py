# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

import hashlib

from sawtooth_rest_api.protobuf import batch_pb2
from sawtooth_rest_api.protobuf import transaction_pb2

from addressing import addresser

from protobuf import payload_pb2
import logging

LOGGER = logging.getLogger(__name__)

def make_create_user_transaction(transaction_signer,
                                               batch_signer,
                                               username,
                                               role,
                                               timestamp):

    agent_address = addresser.get_user_address(transaction_signer.get_public_key().as_hex())

    inputs = [agent_address]

    outputs = [agent_address]

    action = payload_pb2.Create_User(
        username=username,
        role=role)

    payload = payload_pb2.SimpleSupplyPayload(
        action=payload_pb2.SimpleSupplyPayload.CREATE_USER,
        create_user=action,
        timestamp=timestamp)
    payload_bytes = payload.SerializeToString()

    return _make_batch(
        payload_bytes=payload_bytes,
        inputs=inputs,
        outputs=outputs,
        transaction_signer=transaction_signer,
        batch_signer=batch_signer)

def make_drug_import_transaction(transaction_signer,
                                 batch_signer,
                                 timestamp,
                                 id,
                                 name
                                 ):

    user_address = addresser.get_user_address(transaction_signer.get_public_key().as_hex())
    product_address = addresser.get_product_address(id)
    inputs = [user_address, product_address]
    outputs = [product_address]

    action = payload_pb2.DrugImport(
        id=id,
        name=name
        )

    payload = payload_pb2.SimpleSupplyPayload(
        action=payload_pb2.SimpleSupplyPayload.DRUG_IMPORT,
        drug_import=action,
        timestamp=timestamp
    )
    payload_bytes = payload.SerializeToString()

    return _make_batch(
        payload_bytes=payload_bytes,
        inputs=inputs,
        outputs=outputs,
        transaction_signer=transaction_signer,
        batch_signer=batch_signer)

def make_get_drug_transaction(transaction_signer,
                                 batch_signer,
                                 timestamp,
                                 id
                                 ):

    user_address = addresser.get_user_address(transaction_signer.get_public_key().as_hex())
    product_address = addresser.get_product_address(id)
    inputs = [user_address, product_address]
    outputs = [product_address]

    action = payload_pb2.GetDrug(
        id=id
        )

    payload = payload_pb2.SimpleSupplyPayload(
        action=payload_pb2.SimpleSupplyPayload.GET_DRUG,
        get_drug=action,
        timestamp=timestamp
    )
    payload_bytes = payload.SerializeToString()

    return _make_batch(
        payload_bytes=payload_bytes,
        inputs=inputs,
        outputs=outputs,
        transaction_signer=transaction_signer,
        batch_signer=batch_signer)

def make_update_status_transaction(transaction_signer,
                                 batch_signer,
                                 timestamp,
                                 id,
                                 quantity,
                                 price
                                 ):

    user_address = addresser.get_user_address(transaction_signer.get_public_key().as_hex())
    product_address = addresser.get_product_address(id)
    inputs = [user_address, product_address]
    outputs = [product_address]

    action = payload_pb2.UpdateStatus(
        id=id,
        quantity=quantity,
        price=price
        )

    payload = payload_pb2.SimpleSupplyPayload(
        action=payload_pb2.SimpleSupplyPayload.UPDATE_STATUS,
        update_status=action,
        timestamp=timestamp
    )
    payload_bytes = payload.SerializeToString()

    return _make_batch(
        payload_bytes=payload_bytes,
        inputs=inputs,
        outputs=outputs,
        transaction_signer=transaction_signer,
        batch_signer=batch_signer)

def make_update_location_transaction(transaction_signer,
                                 batch_signer,
                                 timestamp,
                                 id,
                                 longitude,
                                 latitude
                                 ):

    user_address = addresser.get_user_address(transaction_signer.get_public_key().as_hex())
    product_address = addresser.get_product_address(id)
    inputs = [user_address, product_address]
    outputs = [product_address]

    action = payload_pb2.UpdateLocation(
        id=id,
        longitude=longitude,
        latitude=latitude
        )

    payload = payload_pb2.SimpleSupplyPayload(
        action=payload_pb2.SimpleSupplyPayload.UPDATE_LOCATION,
        update_location=action,
        timestamp=timestamp
    )
    payload_bytes = payload.SerializeToString()

    return _make_batch(
        payload_bytes=payload_bytes,
        inputs=inputs,
        outputs=outputs,
        transaction_signer=transaction_signer,
        batch_signer=batch_signer)


def _make_batch(payload_bytes,
                inputs,
                outputs,
                transaction_signer,
                batch_signer):

    transaction_header = transaction_pb2.TransactionHeader(
        family_name=addresser.FAMILY_NAME,
        family_version=addresser.FAMILY_VERSION,
        inputs=inputs,
        outputs=outputs,
        signer_public_key=transaction_signer.get_public_key().as_hex(),
        batcher_public_key=batch_signer.get_public_key().as_hex(),
        dependencies=[],
        payload_sha512=hashlib.sha512(payload_bytes).hexdigest())
    transaction_header_bytes = transaction_header.SerializeToString()

    transaction = transaction_pb2.Transaction(
        header=transaction_header_bytes,
        header_signature=transaction_signer.sign(transaction_header_bytes),
        payload=payload_bytes)

    batch_header = batch_pb2.BatchHeader(
        signer_public_key=batch_signer.get_public_key().as_hex(),
        transaction_ids=[transaction.header_signature])
    batch_header_bytes = batch_header.SerializeToString()

    batch = batch_pb2.Batch(
        header=batch_header_bytes,
        header_signature=batch_signer.sign(batch_header_bytes),
        transactions=[transaction])

    return batch