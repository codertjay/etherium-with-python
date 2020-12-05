import json
from web3 import Web3


infura_url = "https://mainnet.infura.io/v3/faa143aa724449f499fb1969621b1cdf"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())