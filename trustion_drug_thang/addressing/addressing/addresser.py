import enum
import hashlib


FAMILY_NAME = 'TRUSTION_DRUG_THANG'
FAMILY_VERSION ='1.0'
NAMESPACE = hashlib.sha512(FAMILY_NAME.encode('utf-8')).hexdigest()[:6]

USER_PREFIX = '00'
PRODUCT_PREFIX = '01'

@enum.unique
class AddressSpace(enum.IntEnum):
    USER_PREFIX = 0
    PRODUCT = 1
    OTHER_FAMILY = 100


def get_user_address(public_key):
    return NAMESPACE + USER_PREFIX + hashlib.sha512(
        public_key.encode('utf-8')).hexdigest()[:62]

def get_product_address(id):
    return NAMESPACE + PRODUCT_PREFIX + hashlib.sha512(
        id.encode('utf-8')).hexdigest()[:62]

def get_address_type(address):
    if address[:len(NAMESPACE)] != NAMESPACE:
        return AddressSpace.OTHER_FAMILY

    infix = address[6:8]

    if infix == '00':
        return AddressSpace.USER_PREFIX
    if infix == '01':
        return AddressSpace.PRODUCT_PREFIX
    return AddressSpace.OTHER_FAMILY