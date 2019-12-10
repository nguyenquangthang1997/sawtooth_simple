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
# ------------------------------------------------------------------------------

from sawtooth_rest_api.messaging import Connection
from sawtooth_rest_api.protobuf import client_batch_submit_pb2
from sawtooth_rest_api.protobuf import validator_pb2

from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory
from sawtooth_signing import secp256k1

from rest_api.errors import ApiBadRequest
from rest_api.errors import ApiInternalError
from rest_api.transaction_creation import \
    make_create_user_transaction
from rest_api.transaction_creation import \
    make_drug_import_transaction
from rest_api.transaction_creation import \
    make_get_drug_transaction
from rest_api.transaction_creation import \
    make_update_status_transaction
from rest_api.transaction_creation import \
    make_update_location_transaction

class Messenger(object):
    def __init__(self, validator_url):
        self._connection = Connection(validator_url)
        self._context = create_context('secp256k1')
        self._crypto_factory = CryptoFactory(self._context)
        self._batch_signer = self._crypto_factory.new_signer(
            self._context.new_random_private_key())

    def open_validator_connection(self):
        self._connection.open()

    def close_validator_connection(self):
        self._connection.close()

    def get_new_key_pair(self):
        private_key = self._context.new_random_private_key()
        public_key = self._context.get_public_key(private_key)
        return public_key.as_hex(), private_key.as_hex()

    async def send_create_user_transaction(self,
                                            private_key,
                                            username,
                                            role,
                                            timestamp):
        transaction_signer = self._crypto_factory.new_signer(
            secp256k1.Secp256k1PrivateKey.from_hex(private_key))

        batch = make_create_user_transaction(
            transaction_signer=transaction_signer,
            batch_signer=self._batch_signer,
            username=username,
            role=role,
            timestamp=timestamp)
        await self._send_and_wait_for_commit(batch)

        return batch

    async def send_drug_import_transaction(self,
                                          private_key,
                                          timestamp,
                                         id,
                                         name
                                        ):
        transaction_signer = self._crypto_factory.new_signer(
            secp256k1.Secp256k1PrivateKey.from_hex(private_key))

        batch = make_drug_import_transaction(
            transaction_signer=transaction_signer,
            batch_signer=self._batch_signer,
            timestamp=timestamp,
            id=id,
            name=name
            )
        await self._send_and_wait_for_commit(batch)

        return batch
    async def send_get_drug_transaction(self,
                                          private_key,
                                          timestamp,
                                         id
                                        ):
        transaction_signer = self._crypto_factory.new_signer(
            secp256k1.Secp256k1PrivateKey.from_hex(private_key))

        batch = make_get_drug_transaction(
            transaction_signer=transaction_signer,
            batch_signer=self._batch_signer,
            timestamp=timestamp,
            id=id
            )
        await self._send_and_wait_for_commit(batch)

        return batch
    async def send_update_status_transaction(self,
                                          private_key,
                                          timestamp,
                                         id,
                                         quantity,
                                         price
                                        ):
        transaction_signer = self._crypto_factory.new_signer(
            secp256k1.Secp256k1PrivateKey.from_hex(private_key))

        batch = make_update_status_transaction(
            transaction_signer=transaction_signer,
            batch_signer=self._batch_signer,
            timestamp=timestamp,
            id=id,
            quantity=quantity,
            price=price
            )
        await self._send_and_wait_for_commit(batch)

        return batch
    async def send_update_location_transaction(self,
                                          private_key,
                                          timestamp,
                                         id,
                                         longitude,
                                         latitude
                                        ):
        transaction_signer = self._crypto_factory.new_signer(
            secp256k1.Secp256k1PrivateKey.from_hex(private_key))

        batch = make_update_location_transaction(
            transaction_signer=transaction_signer,
            batch_signer=self._batch_signer,
            timestamp=timestamp,
            id=id,
            longitude=longitude,
            latitude=latitude
            )
        await self._send_and_wait_for_commit(batch)

        return batch

    async def _send_and_wait_for_commit(self, batch):
        # Send transaction to validator
        submit_request = client_batch_submit_pb2.ClientBatchSubmitRequest(
            batches=[batch])
        await self._connection.send(
            validator_pb2.Message.CLIENT_BATCH_SUBMIT_REQUEST,
            submit_request.SerializeToString())

        # Send status request to validator
        batch_id = batch.header_signature
        status_request = client_batch_submit_pb2.ClientBatchStatusRequest(
            batch_ids=[batch_id], wait=True)
        validator_response = await self._connection.send(
            validator_pb2.Message.CLIENT_BATCH_STATUS_REQUEST,
            status_request.SerializeToString())

        # Parse response
        status_response = client_batch_submit_pb2.ClientBatchStatusResponse()
        status_response.ParseFromString(validator_response.content)
        status = status_response.batch_statuses[0].status
        if status == client_batch_submit_pb2.ClientBatchStatus.INVALID:
            error = status_response.batch_statuses[0].invalid_transactions[0]
            raise ApiBadRequest(error.message)
        elif status == client_batch_submit_pb2.ClientBatchStatus.PENDING:
            raise ApiInternalError('Transaction submitted but timed out')
        elif status == client_batch_submit_pb2.ClientBatchStatus.UNKNOWN:
            raise ApiInternalError('Something went wrong. Try again later')