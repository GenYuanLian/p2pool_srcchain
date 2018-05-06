Requirements:
-------------------------
Generic:
* Srcchain >=1.0.0
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

eg.
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6


Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local srcchaind. For standard
configurations, using P2Pool should be as simple as:

    cd Lyra2Z
    python setup.py install
    python run_p2pool.py --srcchaind-config-path=/your/sourcechain/configfile/path 

Then run your miner program, connecting to 127.0.0.1 on port 9332 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9333 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Contact Developers
-------------------------

Developers are available at:

| Label Name              | Description                                                                                                                                                                                                                                                               |
| :---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gitter                  | [![Join the chat at https://gitter.im/genyuanlian-SourceBlockchain/Lobby](https://badges.gitter.im/genyuanlian-SourceBlockchain/Lobby.svg)](https://gitter.im/genyuanlian-SourceBlockchain/p2pool_srcchain?utm_source=share-link&utm_medium=link&utm_campaign=share-link) |

Issues & PRs management
-------------------------
[![Waffle.io - Columns and their card count](https://badge.waffle.io/GenYuanLian/p2pool_srcchain.svg?columns=all)](https://waffle.io/GenYuanLian/p2pool_srcchain)
[![Throughput Graph](https://graphs.waffle.io/GenYuanLian/p2pool_srcchain/throughput.svg)](https://waffle.io/GenYuanLian/p2pool_srcchain/metrics/throughput)

LICENSE
-------------------------
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
