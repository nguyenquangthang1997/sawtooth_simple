"""
  Author:  BK Blockchain
  Project: ipfs_service
  Created: 09/22/19 10:13
  Purpose: ALL CONFIG VARIABLES FOR IPFS SERVICE PROJECT
"""

import os


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Config:
    DATABASE_DIR = '{}/{}'.format(basedir, 'db')
    HOST = '127.0.0.1'
    PORT = 9000


class IpfsConfig(Config):
    IPFS_PORT = '/ip4/127.0.0.1/tcp/5001/http'


class EtherumNetworkConfig(Config):
    TEST_NET = 'https://ropsten.infura.io/v3/66092b83a4de4330b7cc5df887e3ae4b'
    CONTENT_ID_SAVE_ABI = open('{}/{}/{}/content_id_save_abi.json'.format(basedir, 'config', 'abi'), 'r').read()
    CONTRACT_ADRESS = '0xa4d6Dc08Fa3B9bAF1fF490281bb3E86b36B28eF1'
    PRIVATE_KEY = '0x2AB7D0E36ECEE7CA532E7145CC1392AD8B63863D21F367E46484E55E299FD790'
    ACCOUNT = '0x7f42D55822c420bB4067D26431e0881d882875AE'
    TO = '0xa4d6Dc08Fa3B9bAF1fF490281bb3E86b36B28eF1'
