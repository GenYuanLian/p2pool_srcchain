import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


#P2P_PREFIX = 'f9beb401'.decode('hex') #rbtc args
#P2P_PORT = 10333                      #rbtc args
P2P_PREFIX = 'f9beb402'.decode('hex')  #scchain args
P2P_PORT = 10333                       #scchain args
ADDRESS_VERSION = 0
#RPC_PORT = 8332                       #rbtc args 
RPC_PORT = 10665 #scchain args
# RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            (yield helper.check_genesis_block(bitcoind, '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')) and
#            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
#        ))  #rbtc args
# RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#             (yield helper.check_genesis_block(bitcoind, '00002624dcbee6e76a65f0ae84ac3a4c4f5889722d1412ef92486337fb43a007')) and
#             (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
#         ))  

RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '00000006941e463cf1cb6c74024228810dc81545c854ba5153b117d3bf602204')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        )) #scchain args
		
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
# POW_FUNC = data.hash256
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('Lyra2Z_scrypt').getPoWHash(data))
BLOCK_PERIOD = 600 # s
SYMBOL = 'BTC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoin'), 'bitcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://blockchain.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://blockchain.info/address/'
TX_EXPLORER_URL_PREFIX = 'https://blockchain.info/tx/'
# SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
# SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**16 - 1)
# SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**25 - 1) #rbtc args
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**28 - 1)   #scchain args
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
