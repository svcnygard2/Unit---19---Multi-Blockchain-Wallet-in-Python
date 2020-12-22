#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import subprocess
import json
import os

from constants import BTC, BTCTEST, ETH
from pprint import pprint

from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware

from eth_account import Account


# In[2]:


# Connect Web3
w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER', 'http://localhost:8545')))
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Current block number
w3.eth.blockNumber

# Set Gas Price Strategy
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

# Mnemonic Phrase
mnemonic = os.getenv("MNEMONIC", 'abuse blood note choice garbage spot ice roast smoke yard foster chuckle')


# In[3]:


coin = ETH
mnemonic=mnemonic
depth=3

command = f'php derive -g --mnemonic={mnemonic} --coin={coin} --numderive={depth} --format=json'
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print(output)


# In[4]:


coin='btc-test'
mnemonic=mnemonic
depth=3

command = f'php derive -g --mnemonic="{mnemonic}" --coin={coin}  --numderive={depth} --format=json'
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
keys = json.loads(output)
print(keys)


# In[5]:


coin=BTC
mnemonic=mnemonic
depth=3

command = f'php derive -g --mnemonic="{mnemonic}" --coin={coin}  --numderive={depth} --format=json'
p = subprocess.Popen(
    command,
    stdout=subprocess.PIPE,
    shell=True)
(output, err) = p.communicate()
p_status = p.wait()
keys = json.loads(output)
print(keys)


# In[6]:


def derive_wallets(coin=BTC, mnemonic=mnemonic, depth=3):
    command = f'php derive -g --mnemonic="{mnemonic}" --coin={coin}  --numderive={depth} --format=json'

    p = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        shell=True)
    
    (output, err) = p.communicate()
    p_status = p.wait()
    
    return json.loads(output)


# In[7]:


coins = {
    ETH: derive_wallets(coin=ETH),
    BTCTEST: derive_wallets(coin=BTCTEST),
}
pprint(coins)


# In[8]:


def priv_key_to_account(coin, priv_key):
    if coin == ETH: 
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)


# In[9]:


# Use the private key to send transactions
private_key = coins['eth'][0]['privkey']


# In[10]:


# Account One address saved
account_one = priv_key_to_account(ETH, private_key)
print(account_one.address)
account_one


# In[12]:


# Account Two address saved
account_two = Account.from_key(private_key)
print(account_two.address)
account_two


# In[20]:


# Address balance
w3.eth.getBalance("0xE8871046ea8Ad02D624b8A46b85fBE3A9f4CDD95")

# Send eth to this account address
to = "0xE8871046ea8Ad02D624b8A46b85fBE3A9f4CDD95"


# In[21]:


def create_raw_tx(account, recipient, amount):
   gasEstimate = w3.eth.estimateGas(
       {"from": account.address, "to": recipient, "value": amount}
   )
   return {
       "from": account.address,
       "to": recipient,
       "value": amount,
       "gasPrice": w3.eth.gasPrice,
       "gas": gasEstimate,
       "nonce": w3.eth.getTransactionCount(account.address),
   }


# In[22]:


def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()


# In[23]:


send_tx(account_one, to, 3)

