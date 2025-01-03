[![PyPI version](https://badge.fury.io/py/safe-cli.svg)](https://badge.fury.io/py/safe-cli)
[![Build Status](https://github.com/safe-global/safe-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/safe-global/safe-cli/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/safe-global/safe-cli/badge.svg?branch=main)](https://coveralls.io/github/safe-global/safe-cli?branch=main)
![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)
![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/safeglobal/safe-cli?label=Docker&sort=semver)](https://hub.docker.com/r/safeglobal/safe-cli)

# Safe CLI

Safe CLI is a command-line utility for Safe contracts. You can use it to manage your Safe account from the command line.

It does not rely on Safe{Core} API and can also be used in networks where Safe services are unavailable. Learn more through the [documentation](https://docs.safe.global/advanced/cli-overview).

## Using Docker

**Prerequisite:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

Once Docker is installed on your system, run the following command to create new Safe accounts:

```bash
docker run -it safeglobal/safe-cli safe-creator
```

You can also run the following command to run the Safe CLI with an existing Safe:
```bash
docker run -it safeglobal/safe-cli safe-cli <checksummed_safe_address> <ethereum_node_url>
```

## Using Python PIP

**Prerequisite:** [Python](https://www.python.org/downloads/) >= 3.10 (Python 3.12 is recommended).

Once Python is installed on your system, run the following command to install Safe CLI:
```bash
pip3 install -U safe-cli
```

## Usage

### Safe-Cli

```bash
usage:
 safe-cli [--history] [--get-safes-from-owner] address node_url

 Examples:
 safe-cli 0x0000000000000000000000000000000000000000 https://sepolia.drpc.org
 safe-cli --get-safes-from-owner 0x0000000000000000000000000000000000000000 https://sepolia.drpc.org

 safe-cli --history 0x0000000000000000000000000000000000000000 https://sepolia.drpc.org
 safe-cli --history --get-safes-from-owner 0x0000000000000000000000000000000000000000 https://sepolia.drpc.org

 safe-cli send-ether 0xsafeaddress https://sepolia.drpc.org 0xtoaddress wei-amount --private-key key1 --private-key key1 --private-key keyN [--non-interactive]
 safe-cli send-erc721 0xsafeaddress https://sepolia.drpc.org 0xtoaddress 0xtokenaddres id --private-key key1 --private-key key2 --private-key keyN [--non-interactive]
 safe-cli send-erc20 0xsafeaddress https://sepolia.drpc.org 0xtoaddress 0xtokenaddres wei-amount --private-key key1 --private-key key2 --private-key keyN [--non-interactive]
 safe-cli send-custom 0xsafeaddress https://sepolia.drpc.org 0xtoaddress value 0xtxdata --private-key key1 --private-key key2 --private-key keyN [--non-interactive]

 safe-cli tx-builder 0xsafeaddress https://sepolia.drpc.org  ./path/to/exported/tx-builder/file.json --private-key key1 --private-key keyN [--non-interactive]

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    address       CHECKSUMADDRESS  The address of the Safe, or an owner address if --get-safes-from-owner is specified. [required]                                                                                                                                                                             │
│ *    node_url      TEXT             Ethereum node url. [required]                                                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                                                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Optional Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --history                 --no-history                   Enable history. By default it's disabled due to security reasons [default: no-history]                                                                                                                                                                 │
│ --get-safes-from-owner    --no-get-safes-from-owner      Indicates that address is an owner (Safe Transaction Service is required for this feature) [default: no-get-safes-from-owner]                                                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

 Commands available in unattended mode:

 send-ether
 send-erc20
 send-erc721
 send-custom
 tx-builder
 version

 Use the --help option of each command to see the usage options.
```

To execute transactions unattended, or execute transactions from a json exported from the tx_builder you can use:

```bash
safe-cli send-ether 0xsafeaddress https://sepolia.drpc.org 0xtoaddress wei-amount --private-key key1 --private-key key1 --private-key keyN --non-interactive
safe-cli send-erc721 0xsafeaddress https://sepolia.drpc.org 0xtoaddress 0xtokenaddres id --private-key key1 --private-key key2 --private-key keyN --non-interactive
safe-cli send-erc20 0xsafeaddress https://sepolia.drpc.org 0xtoaddress 0xtokenaddres wei-amount --private-key key1 --private-key key2 --private-key keyN --non-interactive
safe-cli send-custom 0xsafeaddress https://sepolia.drpc.org 0xtoaddress value 0xtxdata --private-key key1 --private-key key2 --private-key keyN --non-interactive

safe-cli tx-builder 0xsafeaddress https://sepolia.drpc.org  ./path/to/exported/tx-builder/file.json --private-key key1 --private-key keyN --non-interactive
```

It is possible to use the environment variable `SAFE_CLI_INTERACTIVE=0` to avoid user interactions. The `--non-interactive` option have more priority than environment variable.

### Safe-Creator

```bash

usage:
        safe-creator [-h] [-v] [--threshold THRESHOLD] [--owners OWNERS [OWNERS ...]] [--safe-contract SAFE_CONTRACT] [--proxy-factory PROXY_FACTORY] [--callback-handler CALLBACK_HANDLER] [--salt-nonce SALT_NONCE] [--without-events] node_url private_key

        Example:
            safe-creator https://sepolia.drpc.org 0000000000000000000000000000000000000000000000000000000000000000


positional arguments:
  node_url              Ethereum node url
  private_key           Deployer private_key

options:
  -h, --help            show this help message and exit
  -v, --version         Show program's version number and exit.
  --threshold THRESHOLD
                        Number of owners required to execute transactions on the created Safe. It mustbe greater than 0 and less or equal than the number of owners
  --owners OWNERS [OWNERS ...]
                        Owners. By default it will be just the deployer
  --safe-contract SAFE_CONTRACT
                        Use a custom Safe master copy
  --proxy-factory PROXY_FACTORY
                        Use a custom proxy factory
  --callback-handler CALLBACK_HANDLER
                        Use a custom fallback handler. It is not required for Safe Master Copies with version < 1.1.0
  --salt-nonce SALT_NONCE
                        Use a custom nonce for the deployment. Same nonce with same deployment configuration will lead to the same Safe address
  --without-events      Use non events deployment of the Safe instead of the regular one. Recommended for mainnet to save gas costs when using the Safe


```

## Safe{Core} API/Protocol

- [Safe Infrastructure](https://github.com/safe-global/safe-infrastructure)
- [Safe Transaction Service](https://github.com/safe-global/safe-transaction-service)
- [Safe Smart Account](https://github.com/safe-global/safe-smart-account)
- [Safe Smart Account deployment info and addresses](https://github.com/safe-global/safe-deployments/tree/main/src/assets)

## Setting up for developing

If you miss something and want to send us a PR:

```bash
git clone https://github.com/safe-global/safe-cli.git
cd safe-cli
stat venv 2>/dev/null || python3 -m venv venv
source venv/bin/activate && pip install -r requirements-dev.txt
pre-commit install -f
```

To run the local version you can install it using:

```bash
pip install .
```

## Contributors

- [Pedro Arias Ruiz](https://github.com/AsiganTheSunk)
- [Uxío Fuentefría](https://github.com/uxio0)
- [Moisés Fernández](https://github.com/moisses89)
