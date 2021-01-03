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
 # Connect Web3 
 w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER", "http://localhost:8545"))) 
 w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
 w3.middleware_onion.inject(geth_poa_middleware, layer=0) 
  
 # Current block number 
 w3.eth.blockNumber 
  
 # Set Gas Price Strategy 
 w3.eth.setGasPriceStrategy(medium_gas_price_strategy) 
  
 # Mnemonic Phrase 
 mnemonic = os.getenv("MNEMONIC" , "abuse blood note choice garbage spot ice roast smoke yard foster chuckle')

 coin = ETH 
 mnemonic=mnemonic 
 depth=3 
  
 command = f'php derive -g --mnemonic={mnemonic} --coin={coin} --numderive={depth} --format=json' 
 p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) 
 (output, err) = p.communicate() 
 pprint(output) 

 coin=BTCTEST 
 mnemonic=mnemonic 
 depth=3 
  
 command = f'php derive -g --mnemonic=\ {mnemonic}\  --coin={coin}  --numderive={depth} --format=json'  ,
 p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
 (output, err) = p.communicate()
 keys = json.loads(output)
 pprint(keys)

 coin=BTC
 mnemonic=mnemonic
 depth=3

 command = f'php derive -g --mnemonic={mnemonic} --coin={coin} --numderive={depth} --format=json'  ,
 p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)  ,
 (output, err) = p.communicate()
 p_status = p.wait()
 keys = json.loads(output)
 pprint(keys) 

 def derive_wallets(coin=BTC, mnemonic=mnemonic, depth=3):
     command = f'php derive -g --mnemonic=\ {mnemonic}\  --coin={coin}  --numderive={depth} --format=json'

     p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) 

     (output, err) = p.communicate()
     p_status = p.wait()

     return json.loads(output) 

 coins = {ETH: derive_wallets(coin=ETH), BTCTEST: derive_wallets(coin=BTCTEST)}
 pprint(coins) 

 def priv_key_to_account(coin, priv_key):
     if coin == ETH:
         return Account.privateKeyToAccount(priv_key)
     if coin == BTCTEST:
         return PrivateKeyTestnet(priv_key) 

 # Use the private key to send transactions
 private_key_eth = coins['eth'][0]['privkey']
 private_key_btctest = coins['btc-test'][0]['privkey'] 

 # ETH account address saved
 eth_account = priv_key_to_account(ETH, private_key_eth)
 print(eth_account.address)

 # Address balance eth
 print(w3.eth.getBalance(eth_account.address))
 eth_account 

 # BTCTEST account address saved
 btctest_account = priv_key_to_account(BTCTEST, private_key_btctest)
 print(btctest_account.address)

 # Address balance btc-test
 print(btctest_account.get_balance('btc'))
 btctest_account 

 # Send btc to this account address
 send_bit = coins['btc-test'][1]['address']
 print(send_bit) 

 # Send eth to this account address (yourself)
 send_eth = coins['eth'][0]['address']
 print(send_eth) 

  def create_raw_tx(coin, account, recipient, amount):
         global tx_data
         if coin == ETH:
             gasEstimate = w3.eth.estimateGas(
                 {from : account.address, to : recipient,  value : amount}
             )
             tx_data = {
                 from : account.address,
                 to : recipient,
                 value : amount,
                 gasPrice : w3.eth.gasPrice,
                 gas : gasEstimate,
                 nonce : w3.eth.getTransactionCount(account.address)
             }
             return tx_data
    
         if coin == BTCTEST:
             return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)]) 

 def send_tx(coin, account, recipient, amount):
     tx = create_raw_tx(coin, account, recipient, amount)
     if coin == ETH:
         print(w3.eth.getBalance(eth_account.address))
         try:
             signed_tx = account.sign_transaction(tx)
             return print(w3.eth.sendRawTransaction(signed_tx.rawTransaction))
         except:
             return print ("Was not able to send"  + f"{coin} coins.")
     if coin == BTCTEST:
         print(account.get_balance('btc'))
         try:
             signed_tx = account.sign_transaction(tx)
             NetworkAPI.broadcast_tx_testnet(signed_tx)
             transaction = account.get_transactions()[0]
             return print("Your Transaction Hash is :"  + f"{transaction}.")
         except:
             return print ("Was not able to send"  + f"{coin} coins.") 

 #send_tx(ETH, eth_account, send_eth, 3) 

 #send_tx(BTCTEST, btctest_account, send_bit, 0.0000001) 