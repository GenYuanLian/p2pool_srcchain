import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


# P2P_PREFIX = '0b110907'.decode('hex')
P2P_PREFIX = '0b110902'.decode('hex')
P2P_PORT = 18333
ADDRESS_VERSION = 111
RPC_PORT = 18332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            # 'bitcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'test'
        ))
SUBSIDY_FUNC = lambda height: 50000*100000000 >> (height + 1)//210000
# POW_FUNC = data.hash256
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('Lyra2Z_scrypt').getPoWHash(data))
BLOCK_PERIOD = 600 # s
SYMBOL = 'BSTK'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoin'), 'bitcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/tx/'
# SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**28 - 1)   #scchain args
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
