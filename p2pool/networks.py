from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    novacoin=math.Object(
        PARENT=networks.nets['novacoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='e037d5b8c6923610'.decode('hex'),
        PREFIX='7208c1a53ef659b0'.decode('hex'),
        P2P_PORT=29946,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=8890,
        BOOTSTRAP_ADDRS='37.57.95.59:8777 81.200.241.54:8777 82.200.205.39:8777 82.234.193.23:8777 85.198.114.251:8777 85.234.62.99:8777 89.239.190.22:8777 89.250.210.94:8777 94.198.0.39:8777 95.84.138.99:8777 109.238.244.73:8777 176.37.148.85:8777 178.19.249.43:8777 178.159.127.151:8777 188.130.184.1:8777 212.98.191.90:8777 212.113.35.38:8777'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60011,
    ),
    novacoin_testnet=math.Object(
        PARENT=networks.nets['novacoin_testnet'],
        SHARE_PERIOD=4, # seconds
        CHAIN_LENGTH=20*60//3, # shares
        REAL_CHAIN_LENGTH=20*60//3, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='e037d5b8c7923110'.decode('hex'),
        PREFIX='7208c1a54ef619b0'.decode('hex'),
        P2P_PORT=18777,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=18336,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60011,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
