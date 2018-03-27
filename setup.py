#!/usr/bin/env python3

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

with open('contrib/requirements/requirements.txt') as f:
    requirements = f.read().splitlines()

with open('contrib/requirements/requirements-hw.txt') as f:
    requirements_hw = f.read().splitlines()

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (3, 5, 0):
    sys.exit("Error: Electron Cash Plus requires Python version >= 3.5.0...")

data_files = ['contrib/requirements/' + r for r in ['requirements.txt', 'requirements-hw.txt']]

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electron-cash-plus-plus.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electron-cash-plus.png'])
    ]

setup(
    name="Electron Cash Plus",
    version=version.PACKAGE_VERSION,
    install_requires=[
        'pyaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
        'jsonrpclib-pelix',
        'PySocks>=1.6.6',
        'pyqt5',
    ],
    extras_require={
        'hardware': requirements_hw,
    },
    packages=[
        'electroncashplus',
        'electroncashplus_gui',
        'electroncashplus_gui.qt',
        'electroncashplus_plugins',
        'electroncashplus_plugins.audio_modem',
        'electroncashplus_plugins.cosigner_pool',
        'electroncashplus_plugins.email_requests',
        'electroncashplus_plugins.hw_wallet',
        'electroncashplus_plugins.keepkey',
        'electroncashplus_plugins.labels',
        'electroncashplus_plugins.ledger',
        'electroncashplus_plugins.trezor',
        'electroncashplus_plugins.digitalbitbox',
        'electroncashplus_plugins.virtualkeyboard',
    ],
    package_dir={
        'electroncashplus': 'lib',
        'electroncashplus_gui': 'gui',
        'electroncashplus_plugins': 'plugins',
    },
    package_data={
        'electroncashplus': [
            'servers.json',
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electron-cash-plus.mo',
        ]
    },
    scripts=['electron-cash-plus'],
    data_files=data_files,
    description="Lightweight Bitcoin Cash Wallet",
    author="Jonald Fyookball",
    author_email="leo@bitcoincashplus.org",
    license="MIT Licence",
    url="http://bitcoincashplus.org",
    long_description="""Lightweight Bitcoin Cash Plus Wallet"""
)
