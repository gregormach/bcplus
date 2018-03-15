# Electron Cash Plus - lightweight Bitcoin Cash client
# Copyright (C) 2011 thomasv@gitorious
# Copyright (C) 2017 Neil Booth
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import os

def read_json_dict(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(path, 'r') as f:
            r = json.loads(f.read())
    except:
        r = {}
    return r

class NetworkConstants:

    # Version numbers for BIP32 extended keys
    # standard: xprv, xpub
    XPRV_HEADERS = {
        'standard': 0x0488ade4,
    }

    XPUB_HEADERS = {
        'standard': 0x0488b21e,
    }

    @classmethod
    def set_mainnet(cls):
        cls.TESTNET = False
        cls.WIF_PREFIX = 0x80
        cls.ADDRTYPE_P2PKH = 28
        cls.ADDRTYPE_P2PKH_BITPAY = 28
        cls.ADDRTYPE_P2SH = 23
        cls.ADDRTYPE_P2SH_BITPAY = 40
        cls.CASHADDR_PREFIX = "bitcoincashplus"
        cls.HEADERS_URL = "http://www.bitcoincashplus.org/files/blockchain_headers"
        cls.GENESIS = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
        cls.DEFAULT_PORTS = {'t': '50001', 's': '50002'}
        cls.DEFAULT_SERVERS = read_json_dict('servers.json')
        cls.TITLE = 'Electron Cash Plus'

        # Bitcoin Cash fork block specification
        cls.BITCOIN_CASHPLUS_FORK_BLOCK_HEIGHT = 509696
        cls.BITCOIN_CASHPLUS_FORK_BLOCK_HASH = "78845aca25c5173784b3854783e09721be4f1d19c743bf778b378132ec0aaf79"



NetworkConstants.set_mainnet()
