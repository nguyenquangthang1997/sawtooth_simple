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
import datetime
from json.decoder import JSONDecodeError
import logging
import time
import json
import uuid

from aiohttp.web import json_response
import bcrypt
import uuid
from Crypto.Cipher import AES
from itsdangerous import BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# defined in [[errors.py]]
from rest_api.errors import ApiBadRequest
from rest_api.errors import ApiNotFound
from rest_api.errors import ApiUnauthorized

# defined in [[elasticsearch.py]]
from rest_api import elasticsearch


# generated from **Protobuf**
from protobuf import user_pb2

from jsonschema import validate
from jsonschema import ValidationError

#from rest_api.ipfs_services.main import *

LOGGER = logging.getLogger(__name__)

role_index_match = {
        "STOKE_KEEPER":"0",
        "NURSE":"1",
        "PATIENT":"2",
    "00":"nothing"
}

role_array= {
        "STOKE_KEEPER",
        "NURSE",
        "PATIENT",
    ""
}

class RouteHandler(object):
    def __init__(self, loop, messenger):
        self._loop = loop
        self._messenger = messenger

    async def drug_import(self, request):
        data_auth = await self._authorize(request)
        role = int(role_index_match[data_auth['role']])

        if role not in [user_pb2.User.PATIENT] :
            return json_response({'status': 'Failure',
                                  'statusCode': 1,
                                  'details': 'Permission denied'})
        private_key = data_auth['private_key']
        body = await decode_request(request)
        instance_validate_type = {'type': 'object', 'properties': {'id': {'type': 'string'}, 'name': {'type': 'string'}}}

        validate_types(instance_validate_type, body)
        required_fields = ['name']
        validate_fields(required_fields, body)

        id = "CREATE"
        name = "CREATE"






        time_11111 = get_time()
        # function params



        id = str(uuid.uuid4())


        name = body.get('name')

        # check exist if type = create
        checkid = await elasticsearch.checkid(id)
        if checkid:
            return json_response({'status': 'Failure',
                                  'statusCode': 3,
                                  'details': ' has been used'})





        #create transaction
        transactionUnique = await self._messenger.send_drug_import_transaction(
            private_key=private_key,
            timestamp = time_11111,
            id=id,
            name=name
 )

        transactionUniqueId = transactionUnique.transactions[0].header_signature


          # save to elasticsearch
        res= await elasticsearch.drug_import(transactionIdBlockchain = transactionUniqueId,
                                                timestamp = time_11111,
                                               id=id,
                                               name=name
                                              )
        return json_response({
        "id":id,

        "status": "Success"
        })
    async def get_drug(self, request):
        required_fields = ['id']
        for field in required_fields:
            try:
                id = request.rel_url.query['id']
            except:
                raise ApiBadRequest(
                " 'id' parameter is required")







        time_11111 = get_time()
        # function params







        #create transaction
        try:
            start123321 = request.rel_url.query['start']
            try:
                start123321 = datetime.datetime.strptime(start123321,"%y/%m/%d")
                start123 = start123321.timestamp()
            except:
                return json_response({'status': 'Failure',
                                  'statusCode': 4,
                                  'details': '"start" must be formatted "year/month/day"'})
        except:
            start123 = -1

        try:
            end123321 = request.rel_url.query['end']

            try:
                end123321 = datetime.datetime.strptime(end123321,"%y/%m/%d")
                end123 = end123321.timestamp()
            except:
                return json_response({'status': 'Failure',
                                  'statusCode': 4,
                                  'details': '"end" must be formatted "year/month/day"'})
        except:
            end123 = -1

        try:
            limit123321 = request.rel_url.query['limit']
            try:
                limit123 = int(limit123321)
                if int(limit123) <= 0:
                    return json_response({'status': 'Failure',
                                  'statusCode': 4,
                                  'details': '"limit" must be greater than 0'})
            except:
                return json_response({'status': 'Failure',
                                  'statusCode': 4,
                                  'details': '"limit" must be a number'})
        except:
            limit123 = -1



        # save to elasticsearch
        res= await elasticsearch.get_drug(
                                               start123 = int(start123),
                                               end123 = int(end123),
                                               limit123 = int(limit123),
                                               id=id
                                              )
        return json_response(
            res
        )
    async def update_status(self, request):
        data_auth = await self._authorize(request)
        role = int(role_index_match[data_auth['role']])

        if role not in [user_pb2.User.PATIENT] :
            return json_response({'status': 'Failure',
                                  'statusCode': 1,
                                  'details': 'Permission denied'})
        private_key = data_auth['private_key']
        body = await decode_request(request)
        instance_validate_type = {'type': 'object', 'properties': {'id': {'type': 'string'}, 'quantity': {'type': 'string'}, 'price': {'type': 'string'}}}

        validate_types(instance_validate_type, body)
        required_fields = ['id','quantity','price']
        validate_fields(required_fields, body)







        time_11111 = get_time()
        # function params



        id = body.get('id')
        quantity = body.get('quantity')
        price = body.get('price')




        #create transaction
        transactionUnique = await self._messenger.send_update_status_transaction(
            private_key=private_key,
            timestamp = time_11111,
            id=id,
            quantity=quantity,
            price=price
 )

        transactionUniqueId = transactionUnique.transactions[0].header_signature


          # save to elasticsearch
        res= await elasticsearch.update_status(transactionIdBlockchain = transactionUniqueId,
                                                timestamp = time_11111,
                                               id=id,
                                               quantity=quantity,
                                               price=price
                                              )
        return json_response({

        "status": "Success"
        })
    async def update_location(self, request):
        data_auth = await self._authorize(request)
        role = int(role_index_match[data_auth['role']])

        if role not in [user_pb2.User.PATIENT] :
            return json_response({'status': 'Failure',
                                  'statusCode': 1,
                                  'details': 'Permission denied'})
        private_key = data_auth['private_key']
        body = await decode_request(request)
        instance_validate_type = {'type': 'object', 'properties': {'id': {'type': 'string'}, 'longitude': {'type': 'string'}, 'latitude': {'type': 'string'}}}

        validate_types(instance_validate_type, body)
        required_fields = ['id','longitude','latitude']
        validate_fields(required_fields, body)







        time_11111 = get_time()
        # function params



        id = body.get('id')
        longitude = body.get('longitude')
        latitude = body.get('latitude')




        #create transaction
        transactionUnique = await self._messenger.send_update_location_transaction(
            private_key=private_key,
            timestamp = time_11111,
            id=id,
            longitude=longitude,
            latitude=latitude
 )

        transactionUniqueId = transactionUnique.transactions[0].header_signature


          # save to elasticsearch
        res= await elasticsearch.update_location(transactionIdBlockchain = transactionUniqueId,
                                                timestamp = time_11111,
                                               id=id,
                                               longitude=longitude,
                                               latitude=latitude
                                              )
        return json_response({

        "status": "Success"
        })

    async def create_user(self, request):
        """
        Add new user to organization. <br>
        **Input**:<br>
            request: HTTP request <br>
        NOTE: <br>
         - Require field name, username, password, number_phone, address, role  <br>
         - Org need to login in earlier <br>
        """
        body = await decode_request(request)
        required_fields = ['username','password','role']
        validate_fields(required_fields, body)

        schema = {"type":"object", "properties":{"username":{"type":"string"},"password":{"type":"string"},"role":{"type":"string"} }}
        validate_types(schema, body)

        public_key, private_key = self._messenger.get_new_key_pair()
        user_id = str(uuid.uuid4())
        role = body.get('role').upper()
        username = body.get('username')
        user = await elasticsearch.getUserByUsername(username)
        if user:
            return json_response({'status': 'Failure',
                                  'statusCode': 3,
                                  'details': 'Username already existed'})
        if role not in role_array:
            return json_response({'status': 'Failure',
                                  'statusCode': 3,
                                  'details': 'Role not in list roles'})

        transactionUnique = await self._messenger.send_create_user_transaction(
            private_key=private_key,
            username=body.get('username'),
            role=role,
            timestamp=get_time(),
        )

        transactionUniqueId = transactionUnique.transactions[0].header_signature
        encrypted_private_key = encrypt_private_key(
            request.app['aes_key'], public_key, private_key)
        hashed_password = hash_password(body.get('password'))

        await elasticsearch.createUser(
            username=body.get('username'),
            role=role,
            hashed_password=hashed_password,
            encrypted_private_key=encrypted_private_key,
            public_key=public_key,
            transactionIdBlockchain = transactionUniqueId
        )

        return json_response({
            "status": "Success",
            "statusCode": 0,
            "details": "User created",
            "userId":user_id
        })
    async def query_elasticsearch(self, request):
        body = await decode_request(request)
        data_return =  await elasticsearch.query_elasticsearch(body = body)
        return json_response(data_return)



    async def authenticate(self, request):
        """
        Handle login user request.<br/>
        **Input**:<br/>
            request(body: json, require username and password field).<br/>
        Return a token if login success.<br/>
        """
        body = await decode_request(request)
        required_fields = ['username', 'password']
        validate_fields(required_fields, body)

        schema = {"type":"object", "properties":{"username":{"type":"string"},"password":{"type":"string"}}}
        validate_types(schema, body)

        password = bytes(body.get('password'), 'utf-8')

        user = await elasticsearch.getUserByUsername(body.get('username'))
        if len(user) == 0:
            return json_response({'status': 'Failure',
                                 'statusCode': 2,
                                 'details': 'Username does not exist'})

        hashed_password = user['hashed_password']
        if not bcrypt.checkpw(password, bytes.fromhex(hashed_password)):
            return json_response({'status': 'Failure',
                                 'statusCode': 4,
                                 'details': 'Wrong password'})

        token = generate_auth_token(
            request.app['secret_key'], user['username'])

        return json_response({"result": "Success", "statusCode": 0, 'authorization': token})



    async def _authorize(self, request):
        token = request.headers.get('AUTHORIZATION')
        if token is None:
            raise ApiUnauthorized('No auth token provided')
        token_prefixes = ('Bearer', 'Token')
        for prefix in token_prefixes:
            if prefix in token:
                token = token.partition(prefix)[2].strip()
        try:
            token_dict = deserialize_auth_token(request.app['secret_key'],
                                                token)
        except BadSignature:
            raise ApiUnauthorized('Invalid auth token')
        username = token_dict.get('username')

        user = await elasticsearch.getUserByUsername(username)
        if len(user) == 0:
            raise ApiUnauthorized('Token is not associated with an user')
        role = user['role']
        return {'role': role, 'private_key': decrypt_private_key(request.app['aes_key'],
                                                                 user['public_key'],
                                                                 user['encrypted_private_key'])}


async def decode_request(request):
    try:
        return await request.json()
    except JSONDecodeError:
        raise ApiBadRequest('Improper JSON format')


def validate_fields(required_fields, body):
    for field in required_fields:
        if body.get(field) is None:
            raise ApiBadRequest(
                "'{}' parameter is required".format(field))

def validate_types(schema, body):
    try:
        validate(instance=body, schema=schema)
    except ValidationError as e:
        string_array_error = str(e).split("\n")
        array = {"On instance","[","]","'",":"," "}
        for a in array:
            string_array_error[5] = string_array_error[5].replace(a,"")
        message = string_array_error[0]+" on field '"+ string_array_error[5] +"'"

        raise ApiBadRequest(message)


def encrypt_private_key(aes_key, public_key, private_key):
    init_vector = bytes.fromhex(public_key[:32])
    cipher = AES.new(bytes.fromhex(aes_key), AES.MODE_CBC, init_vector)
    return cipher.encrypt(private_key)


def decrypt_private_key(aes_key, public_key, encrypted_private_key):
    init_vector = bytes.fromhex(public_key[:32])
    cipher = AES.new(bytes.fromhex(aes_key), AES.MODE_CBC, init_vector)
    private_key = cipher.decrypt(bytes.fromhex(encrypted_private_key))
    return private_key


def hash_password(password):
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def get_time():
    dts = datetime.datetime.utcnow()
    return round(time.mktime(dts.timetuple()) + dts.microsecond/1e6)


def generate_auth_token(secret_key, username):
    serializer = Serializer(secret_key)
    token = serializer.dumps({'username': username})
    return token.decode('ascii')


def deserialize_auth_token(secret_key, token):
    serializer = Serializer(secret_key)
    return serializer.loads(token)
