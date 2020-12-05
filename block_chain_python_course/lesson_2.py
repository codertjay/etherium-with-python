from web3 import Web3

# in here i am using genache url for this project

genache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(genache_url))

account_1 = ""
account_2 = ""

private_key = ""

nance = web3.eth.getTransaction(account_1)

tx = {
    'nance': '',
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 200000,  # unit of gas
    'gasPrice': web3.toWei('50', 'gwei')

}
# build a transaction

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)

print(web3.toHex)