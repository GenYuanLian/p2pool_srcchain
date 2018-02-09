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
To use P2Pool, you must be running your own local bitcoind. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --bitcoind-config-path=/your/sourcechain/configfile/path

Then run your miner program, connecting to 127.0.0.1 on port 9332 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9333 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help
